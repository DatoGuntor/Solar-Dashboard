import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils.data_handler import load_metrics_data, load_sample_data
from utils.visualization import create_model_comparison_plot, create_performance_radar
from components.metrics import display_metrics

# Set page config
st.set_page_config(page_title="Solar Power Forecasting Dashboard", layout="wide")

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
st.markdown(
    "<div class='header'>"
    "<h1>SOLAR POWER FORECASTING - MODEL PERFORMANCE DASHBOARD YEAR 2022</h1>"
    "</div>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown("### Model Selection")
    
    # Model buttons with consistent styling
    models = ["U-LSTM", "M-LSTM (Wsensor)", "M-LSTM (Wsensor+MET)", "Bi-LSTM",
             "CNN", "GRU", "LSTM-CNN", "LSTM-GRU"]
    
    selected_model = None
    for model in models:
        if st.button(model, key=f"btn_{model}", use_container_width=True):
            selected_model = model
    
    st.markdown("---")
    
    # Model comparison button
    if st.button("Model Comparison", key="btn_comparison", use_container_width=True):
        st.session_state.show_comparison = True
    
    # Default to first model if none selected
    if selected_model is None:
        selected_model = models[0]

# Load data
metrics_data = load_metrics_data()
time_series_data = load_sample_data(selected_model)

# Main content
if st.session_state.get('show_comparison', False):
    col2 = st.empty()  # Placeholder for col2
    # Model comparison view
    # st.markdown("### Model Performance Comparison")
    
    # Combined time series plot
    st.markdown("## Comparing All Models")
    all_models_data = {}
    for model in models:
        all_models_data[model] = load_sample_data(model)
    
    fig = go.Figure()
    for model in models:
        data = all_models_data[model]
        fig.add_trace(go.Scatter(
            x=data['Time'],
            y=data['Predicted'],
            name=f'{model} (Predicted)',
            line=dict(dash='dash')
        ))
    
    # Add actual values from any model (they're all the same)
    fig.add_trace(go.Scatter(
        x=data['Time'],
        y=data['Actual'],
        name='Actual',
        line=dict(color='#1E88E5', width=2)
    ))

    fig.update_layout(
        title=dict(
            text=f"Actual vs Predicted Values Over the Test Set",
            font=dict(size=20)  # Adjust title font size
        ),
        xaxis=dict(
            title=dict(text="Time (minutes)", font=dict(size=20)),  # X-axis title font size
            tickfont=dict(size=18),  # X-axis tick labels font size
            range=[0,550]
        ),
        yaxis=dict(
            title=dict(text="Solar Power (kW)", font=dict(size=20)),  # Y-axis title font size
            tickfont=dict(size=18)  # Y-axis tick labels font size
        ),
        legend=dict(
            font=dict(size=18)  # Legend font size
        ),
        font=dict(size=18),  # Global font settings
        hovermode='x unified',
        showlegend=True,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Metrics comparison - All metrics in one row
    st.markdown("### Model Performance Metrics Comparison")
    metric_cols = st.columns(4)
    metrics = ["MAE (kW)", "MSE (kW)", "RMSE (kW)", "R²"]
    
    # Use a consistent color palette for models
    model_colors = px.colors.qualitative.Set2
    
    for idx, metric in enumerate(metrics):
        with metric_cols[idx]:
            fig = create_model_comparison_plot(metrics_data, metric, model_colors)
            st.plotly_chart(fig, use_container_width=True)
    
    # Reset comparison view
    if st.button("Back to Single Model View"):
        st.session_state.show_comparison = False
        st.rerun()
else:
    col1, col2 = st.columns([7, 3])
    
    with col1:
        # Time series plot
        from components.plots import create_time_series
        st.plotly_chart(
            create_time_series(time_series_data, selected_model),
            use_container_width=True
        )
        
        # Lower plots
        col1_1, col1_2 = st.columns(2)
        from components.plots import create_bar_comparison, create_scatter_plot
        with col1_1:
            st.plotly_chart(
                create_bar_comparison(time_series_data, selected_model),
                use_container_width=True
            )
        with col1_2:
            st.plotly_chart(
                create_scatter_plot(time_series_data, selected_model),
                use_container_width=True
            )


with col2:
    # Display metrics
    display_metrics(metrics_data, selected_model)
