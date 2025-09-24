"""
Real-time Stock Dashboard using Streamlit
Interactive web interface for the Stock Tracker
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import os
from stock_tracker import StockTracker

# Configure Streamlit page
st.set_page_config(
    page_title="📊 Interactive Stock Tracker",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_portfolio_data():
    """Load portfolio data from Excel files"""
    try:
        portfolio_file = "Portfolio_Summary.xlsx"
        if os.path.exists(portfolio_file):
            return pd.read_excel(portfolio_file)
        else:
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading portfolio data: {str(e)}")
        return pd.DataFrame()

def load_historical_data():
    """Load consolidated historical data"""
    try:
        historical_file = "Consolidated_Historical_Data.xlsx"
        if os.path.exists(historical_file):
            return pd.read_excel(historical_file)
        else:
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading historical data: {str(e)}")
        return pd.DataFrame()

def create_price_chart(data, symbols):
    """Create interactive price chart"""
    fig = go.Figure()
    
    for symbol in symbols:
        symbol_data = data[data['Symbol'] == symbol]
        if not symbol_data.empty:
            fig.add_trace(go.Scatter(
                x=symbol_data['Date'],
                y=symbol_data['Close'],
                mode='lines',
                name=symbol,
                line=dict(width=2),
                hovertemplate=f'<b>{symbol}</b><br>Date: %{{x}}<br>Price: $%{{y:.2f}}<extra></extra>'
            ))
    
    fig.update_layout(
        title="Stock Price Trends",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        height=400,
        hovermode='x unified',
        showlegend=True
    )
    
    return fig

def create_returns_chart(data, symbols):
    """Create cumulative returns chart"""
    fig = go.Figure()
    
    for symbol in symbols:
        symbol_data = data[data['Symbol'] == symbol]
        if not symbol_data.empty:
            fig.add_trace(go.Scatter(
                x=symbol_data['Date'],
                y=symbol_data['Cumulative_Return'] * 100,
                mode='lines',
                name=f"{symbol} Returns",
                line=dict(width=2),
                hovertemplate=f'<b>{symbol}</b><br>Date: %{{x}}<br>Return: %{{y:.2f}}%<extra></extra>'
            ))
    
    fig.update_layout(
        title="Cumulative Returns (%)",
        xaxis_title="Date",
        yaxis_title="Cumulative Return (%)",
        height=400,
        hovermode='x unified',
        showlegend=True
    )
    
    return fig

def create_volume_chart(data, symbols):
    """Create volume chart"""
    fig = make_subplots(
        rows=len(symbols), cols=1,
        subplot_titles=[f"{symbol} Volume" for symbol in symbols],
        shared_xaxes=True,
        vertical_spacing=0.05
    )
    
    for i, symbol in enumerate(symbols, 1):
        symbol_data = data[data['Symbol'] == symbol]
        if not symbol_data.empty:
            fig.add_trace(
                go.Bar(
                    x=symbol_data['Date'],
                    y=symbol_data['Volume'],
                    name=f"{symbol} Volume",
                    showlegend=False
                ),
                row=i, col=1
            )
    
    fig.update_layout(height=200 * len(symbols), title="Trading Volume")
    return fig

def create_performance_metrics_table(portfolio_data):
    """Create performance metrics table"""
    if portfolio_data.empty:
        return pd.DataFrame()
    
    # Calculate additional metrics
    portfolio_data['Price_Change'] = portfolio_data['Current_Price'] - (portfolio_data['Current_Price'] / (1 + portfolio_data['Daily_Return_Pct']/100))
    portfolio_data['Price_Change_$'] = portfolio_data['Price_Change'].round(2)
    
    # Format for display
    display_data = portfolio_data.copy()
    display_data['Current_Price'] = display_data['Current_Price'].apply(lambda x: f"${x:.2f}")
    display_data['Daily_Return_Pct'] = display_data['Daily_Return_Pct'].apply(lambda x: f"{x:.2f}%")
    display_data['Cumulative_Return_Pct'] = display_data['Cumulative_Return_Pct'].apply(lambda x: f"{x:.2f}%")
    display_data['Volume'] = display_data['Volume'].apply(lambda x: f"{x:,}")
    
    return display_data

def main():
    """Main Streamlit app"""
    
    # Header
    st.title("📊 Interactive Stock Tracker Dashboard")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("🎛️ Controls")
    
    # Update data button
    if st.sidebar.button("🔄 Update Stock Data", type="primary"):
        with st.spinner("Fetching latest stock data..."):
            tracker = StockTracker(['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT'])
            success = tracker.run_update()
            
            if success:
                st.sidebar.success("✅ Data updated successfully!")
                st.experimental_rerun()
            else:
                st.sidebar.error("❌ Failed to update data")
    
    # Load data
    portfolio_data = load_portfolio_data()
    historical_data = load_historical_data()
    
    if portfolio_data.empty:
        st.warning("⚠️ No portfolio data found. Please click 'Update Stock Data' to fetch the latest information.")
        return
    
    # Symbol selector
    available_symbols = portfolio_data['Symbol'].unique().tolist() if not portfolio_data.empty else []
    selected_symbols = st.sidebar.multiselect(
        "📈 Select ETFs to Display",
        options=available_symbols,
        default=available_symbols
    )
    
    if not selected_symbols:
        st.warning("Please select at least one ETF symbol from the sidebar.")
        return
    
    # Main dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    # Key metrics
    filtered_portfolio = portfolio_data[portfolio_data['Symbol'].isin(selected_symbols)]
    
    with col1:
        total_symbols = len(filtered_portfolio)
        st.metric("📊 Tracked ETFs", total_symbols)
    
    with col2:
        avg_daily_return = filtered_portfolio['Daily_Return_Pct'].mean()
        st.metric("📈 Avg Daily Return", f"{avg_daily_return:.2f}%")
    
    with col3:
        best_performer = filtered_portfolio.loc[filtered_portfolio['Daily_Return_Pct'].idxmax(), 'Symbol'] if not filtered_portfolio.empty else "N/A"
        st.metric("🏆 Best Performer", best_performer)
    
    with col4:
        last_updated = filtered_portfolio['Last_Updated'].iloc[0] if not filtered_portfolio.empty else "N/A"
        st.metric("🕒 Last Updated", str(last_updated))
    
    st.markdown("---")
    
    # Charts section
    if not historical_data.empty:
        filtered_historical = historical_data[historical_data['Symbol'].isin(selected_symbols)]
        
        # Price trends
        st.subheader("📈 Stock Price Trends")
        price_chart = create_price_chart(filtered_historical, selected_symbols)
        st.plotly_chart(price_chart, use_container_width=True)
        
        # Returns
        st.subheader("💹 Cumulative Returns")
        returns_chart = create_returns_chart(filtered_historical, selected_symbols)
        st.plotly_chart(returns_chart, use_container_width=True)
        
        # Volume (collapsible)
        with st.expander("📊 Trading Volume Analysis"):
            volume_chart = create_volume_chart(filtered_historical, selected_symbols)
            st.plotly_chart(volume_chart, use_container_width=True)
    
    # Performance table
    st.subheader("📋 Current Performance Metrics")
    performance_table = create_performance_metrics_table(filtered_portfolio)
    
    if not performance_table.empty:
        st.dataframe(
            performance_table[['Symbol', 'Current_Price', 'Daily_Return_Pct', 'Cumulative_Return_Pct', 'Volume']],
            use_container_width=True
        )
    
    # Additional insights
    st.markdown("---")
    st.subheader("🔍 Portfolio Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top gainers
        if not filtered_portfolio.empty:
            top_gainer = filtered_portfolio.loc[filtered_portfolio['Daily_Return_Pct'].idxmax()]
            st.success(f"🚀 **Top Gainer**: {top_gainer['Symbol']} (+{top_gainer['Daily_Return_Pct']:.2f}%)")
    
    with col2:
        # Top losers
        if not filtered_portfolio.empty:
            top_loser = filtered_portfolio.loc[filtered_portfolio['Daily_Return_Pct'].idxmin()]
            if top_loser['Daily_Return_Pct'] < 0:
                st.error(f"📉 **Top Loser**: {top_loser['Symbol']} ({top_loser['Daily_Return_Pct']:.2f}%)")
            else:
                st.info(f"📊 **Lowest Gainer**: {top_loser['Symbol']} (+{top_loser['Daily_Return_Pct']:.2f}%)")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>🔄 Data updates automatically when you click 'Update Stock Data'</p>
            <p>📊 Integrates seamlessly with your Power BI dashboard</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()