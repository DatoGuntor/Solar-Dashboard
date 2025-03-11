# SolarDashboard
The Solar Power Forecasting Dashboard is an interactive web-based application designed to provide accurate solar energy predictions. Built using a modular and scalable structure, the dashboard integrates multiple predictive models, real-time data visualization, and performance analytics.

Scope of Work:

Dashboard Development:

Implementation of a modular Streamlit-based interface
Integration of Plotly for interactive visualizations
Development of Pandas and NumPy-powered data handling
Functional Components:

Left Sidebar: Model selection for eight predictive models with a comparison mode
Main Content Area: Time series visualization with additional comparative insights
Right Panel: Performance metric display including MAE, MSE, RMSE, and R²
Code Structure & Maintainability:

Modular architecture with separate files for visualizations, metrics, and data processing
Custom CSS for a professional and responsive design
Scalable structure suitable for deployment on Railway.com
Technology Stack:

Programming Language: Python
Framework: Streamlit
Visualization: Plotly
Data Processing: Pandas, NumPy
Styling: HTML/CSS (custom.css)
Configuration: JSON & TOML
Deliverables:

Fully functional Solar Power Forecasting Dashboard
Source code with clear documentation
Deployment assistance (if required)


# Solar Power Forecasting Dashboard - User Manual

## Overview
This dashboard provides an interactive interface for analyzing and comparing the performance of various solar power forecasting models. The interface is divided into three main sections: the sidebar for model selection, the main visualization area, and the performance metrics panel.

## Navigation

### Sidebar - Model Selection
- Choose from 8 different deep learning models:
  - U-LSTM
  - M-LSTM (Wsensor)
  - M-LSTM (Wsensor+MET)
  - Bi-LSTM
  - CNN
  - GRU
  - LSTM-CNN
  - LSTM-GRU
- Click the "Model Comparison" button at the bottom to view all models simultaneously

### Main Visualization Area

#### Time Series Plot (Main Graph)
- Blue solid line: Actual solar power values
- Orange dashed line: Predicted values
- X-axis: Time in minutes
- Y-axis: Solar power output in kilowatts (kW)
- Hover over the lines to see exact values

#### Bar Chart (Lower Left)
- Displays the first 5 test data points
- Blue bars: Actual values
- Orange bars: Predicted values
- Helps visualize prediction accuracy for specific time points

#### Scatter Plot (Lower Right)
- X-axis: Actual values
- Y-axis: Predicted values
- Red dashed line: Regression line
- Perfect predictions would lie on the diagonal
- Helps visualize overall prediction accuracy

### Performance Metrics Panel (Right Side)

The dashboard displays four key performance metrics:

1. Mean Absolute Error (MAE)
   - Measures average absolute difference between predictions and actual values
   - Lower values indicate better performance
   - Unit: kilowatts (kW)

2. Mean Squared Error (MSE)
   - Measures average squared difference between predictions and actual values
   - Penalizes larger errors more heavily
   - Unit: kilowatts squared (kW²)

3. Root Mean Squared Error (RMSE)
   - Square root of MSE
   - Provides error measure in same unit as original data
   - Unit: kilowatts (kW)

4. R² Score (Coefficient of Determination)
   - Measures proportion of variance in actual values explained by predictions
   - Range: 0 to 1 (higher is better)
   - 1 indicates perfect predictions

## Model Comparison View

Access the model comparison view by clicking the "Model Comparison" button in the sidebar:

1. Combined Time Series Plot
   - Shows predictions from all models simultaneously
   - Each model's predictions shown as dashed lines
   - Actual values shown as solid blue line
   - Helps visualize relative performance across models

2. Performance Metrics Comparison
   - Bar charts comparing all models across each metric
   - Helps identify best-performing models for different metrics

3. Return to Single Model View
   - Click "Back to Single Model View" button to exit comparison mode

## Tips for Effective Use

1. Start by examining individual models to understand their performance characteristics
2. Use the comparison view to identify the best model for your needs
3. Consider multiple metrics when evaluating model performance
4. Hover over plots to see exact values
5. Pay attention to both overall trends and specific time points

## Interpreting Results

- Lower values are better for MAE, MSE, and RMSE
- Higher values are better for R² Score
- Look for consistent performance across different metrics
- Consider both accuracy (metrics) and visual fit (plots)

This dashboard helps you make informed decisions about which solar power forecasting model best suits your needs by providing comprehensive performance analysis and visualization tools.
