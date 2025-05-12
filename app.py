import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Virat Kohli's Test Cricket Legacy",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .header-style {
        font-size: 32px;
        font-weight: bold;
        color: #1E3C72;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader-style {
        font-size: 24px;
        font-weight: bold;
        color: #2E5090;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .card {
        border-radius: 5px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        padding: 16px;
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #1E3C72;
    }
    .metric-label {
        font-size: 16px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="header-style">Virat Kohli: The Complete Test Cricket Legacy</div>', unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Career Overview", "Performance Analysis", "Captaincy Record", "Comparative Analysis", "Legacy"])

# Create dataframes from the PDF data
# Career statistics by year
yearly_stats = pd.DataFrame({
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Matches': [5, 9, 8, 10, 9, 12, 10, 13, 8, 3, 10, 7, 6, 5],
    'Innings': [8, 15, 16, 19, 15, 18, 16, 24, 11, 6, 19, 13, 11, 9],
    'Runs': [202, 689, 616, 847, 640, 1215, 1059, 1322, 612, 116, 536, 265, 557, 392],
    'Average': [25.25, 49.21, 41.06, 47.05, 45.71, 75.93, 75.64, 55.08, 68.00, 19.33, 28.21, 20.38, 55.70, 43.55],
    'Hundreds': [0, 3, 1, 3, 2, 4, 5, 5, 2, 0, 0, 0, 2, 1],
    'Fifties': [2, 2, 4, 3, 3, 2, 1, 5, 2, 0, 4, 0, 1, 1]
})

# Performance against different opposition
opposition_stats = pd.DataFrame({
    'Opposition': ['Australia', 'Bangladesh', 'England', 'New Zealand', 'South Africa', 'Sri Lanka', 'West Indies', 'Afghanistan', 'Zimbabwe'],
    'Matches': [25, 5, 28, 9, 14, 10, 15, 1, 1],
    'Innings': [43, 6, 52, 15, 24, 16, 23, 1, 1],
    'Runs': [1979, 392, 1991, 830, 1236, 1025, 898, 0, 3],
    'Average': [48.26, 78.40, 39.82, 59.28, 56.18, 73.21, 44.90, 0.00, 3.00],
    'Hundreds': [8, 2, 5, 3, 3, 5, 2, 0, 0],
    'Fifties': [5, 0, 10, 3, 5, 2, 4, 0, 0]
})

# Home vs Away performance
venue_stats = pd.DataFrame({
    'Venue': ['Home', 'Away', 'Neutral'],
    'Matches': [52, 56, 5],
    'Innings': [83, 96, 11],
    'Runs': [4318, 3903, 455],
    'Average': [61.69, 42.42, 45.50],
    'Hundreds': [18, 10, 1],
    'Fifties': [11, 15, 3]
})

# Performance in different match results
result_stats = pd.DataFrame({
    'Result': ['Wins', 'Losses', 'Draws'],
    'Matches': [44, 29, 40],
    'Innings': [69, 56, 65],
    'Runs': [4065, 1822, 2789],
    'Average': [67.75, 33.74, 45.72],
    'Hundreds': [16, 5, 8],
    'Fifties': [12, 8, 9]
})

# Performance in different career phases
phase_stats = pd.DataFrame({
    'Phase': ['Early Career', 'Rise to Prominence', 'Peak Performance', 'Decline Phase', 'Revival Phase'],
    'Period': ['2011-2013', '2014-2015', '2016-2019', '2020-2022', '2023-2025'],
    'Matches': [22, 19, 43, 20, 9],
    'Runs': [1507, 1487, 4208, 917, 557],
    'Average': [39.65, 46.46, 66.47, 24.13, 55.70],
    'Hundreds': [4, 5, 16, 0, 2],
    'Fifties': [8, 6, 10, 4, 1]
})

# Captaincy record overall
captaincy_stats = pd.DataFrame({
    'Category': ['Tests as Captain', 'Won', 'Lost', 'Drawn', 'Win %'],
    'Value': [68, 40, 17, 11, 58.8]
})

# Captaincy record by venue
captaincy_venue = pd.DataFrame({
    'Venue': ['Home', 'Away', 'Neutral'],
    'Matches': [31, 32, 5],
    'Won': [24, 14, 2],
    'Lost': [2, 14, 1],
    'Drawn': [5, 4, 2],
    'Win %': [77.4, 43.7, 40.0]
})

# Captaincy record by opposition
captaincy_opposition = pd.DataFrame({
    'Opposition': ['Australia', 'Bangladesh', 'England', 'New Zealand', 'South Africa', 'Sri Lanka', 'West Indies', 'Afghanistan'],
    'Matches': [15, 4, 12, 6, 10, 9, 11, 1],
    'Won': [8, 3, 5, 3, 5, 9, 7, 0],
    'Lost': [6, 0, 5, 2, 4, 0, 0, 0],
    'Drawn': [1, 1, 2, 1, 1, 0, 4, 1],
    'Win %': [53.3, 75.0, 41.7, 50.0, 50.0, 100.0, 63.6, 0.0]
})

# Personal performance as captain
captain_batting = pd.DataFrame({
    'Category': ['Tests', 'Innings', 'Runs', 'Average', '100s', '50s', 'Highest Score'],
    'Value': [68, 113, 5864, 54.80, 20, 18, '254*']
})

# Comparison with contemporaries
contemporary_comparison = pd.DataFrame({
    'Batsman': ['Virat Kohli', 'Steve Smith', 'Joe Root', 'Kane Williamson', 'Babar Azam'],
    'Tests': [113, 105, 138, 99, 52],
    'Runs': [8676, 9525, 11416, 8675, 3696],
    'Average': [49.29, 58.83, 50.07, 54.87, 43.48],
    'Hundreds': [29, 32, 31, 29, 9],
    'Fifties': [29, 38, 61, 33, 26]
})

# Comparison with Indian legends
indian_legends = pd.DataFrame({
    'Batsman': ['Virat Kohli', 'Sachin Tendulkar', 'Rahul Dravid', 'Sunil Gavaskar', 'VVS Laxman', 'Virender Sehwag', 'MS Dhoni'],
    'Tests': [113, 200, 163, 125, 134, 103, 90],
    'Runs': [8676, 15921, 13288, 10122, 8781, 8503, 4876],
    'Average': [49.29, 53.78, 52.31, 51.12, 45.97, 49.43, 38.09],
    'Hundreds': [29, 51, 36, 34, 17, 23, 6],
    'Fifties': [29, 68, 63, 45, 56, 32, 33]
})

# Technical evolution data
technical_evolution = pd.DataFrame({
    'Aspect': ['Stance', 'Backlift', 'Footwork', 'Off-side Play', 'On-side Play', 'Defense', 'Attack vs Spin', 'Attack vs Pace'],
    'Early Career (2011-13)': ['More upright, narrower', 'Higher, more pronounced', 'Occasionally tentative', 'Vulnerable outside off', 'Strong, natural', 'Developing solidity', 'Aggressive, risky', 'Counter-attacking'],
    'Mid Career (2014-19)': ['Slightly crouched, wider', 'More controlled, efficient', 'Decisive, confident', 'Dominant, controlled', 'Powerful, dominant', 'Rock solid', 'Calculated, dominant', 'Controlling, authoritative'],
    'Late Career (2020-25)': ['More balanced, compact', 'Shortened, quicker', 'Strategic, economical', 'Selective, disciplined', 'Refined, calculated', 'Adaptive to conditions', 'Strategic, selective', 'Experience-driven']
})

# Shot selection evolution
shot_evolution = pd.DataFrame({
    'Shot': ['Cover Drive', 'Straight Drive', 'Flick', 'Cut', 'Pull/Hook', 'Defensive', 'Glance'],
    'Early Career %': [18.5, 9.2, 14.8, 8.3, 7.1, 32.4, 9.7],
    'Mid Career %': [14.2, 12.5, 17.6, 10.2, 8.5, 28.2, 8.8],
    'Late Career %': [10.5, 8.6, 20.4, 11.8, 6.2, 35.6, 6.9],
    'Effectiveness': ['High Risk/High Reward', 'High Control', 'High Control', 'Medium Control', 'Medium Risk', 'High Control', 'High Control']
})

# Dismissal pattern
dismissal_pattern = pd.DataFrame({
    'Dismissal Type': ['Caught', 'Bowled', 'LBW', 'Run Out', 'Stumped'],
    'Count': [129, 26, 24, 3, 2],
    'Percentage': [70.1, 14.1, 13.0, 1.6, 1.1],
    'Average Before Dismissal': [50.12, 31.25, 33.45, 41.30, 24.50]
})

# Legacy impact metrics
legacy_impact = pd.DataFrame({
    'Impact Area': ['Technical Innovation', 'Mental Approach', 'Fitness Standards', 'Fast Bowling Culture', 
                   'Team Overseas Performance', 'Aggressive Captaincy', 'Youth Inspiration', 'Commercial Impact'],
    'Score (1-10)': [7, 9, 10, 9, 8, 10, 10, 10],
    'Key Evidence': ['Revolutionized cover drive technique', 'Changed team\'s winning mindset', 
                    'Complete fitness revolution in Indian cricket', 'Developed India\'s best ever pace attack',
                    'First Indian team to win in Australia', 'Highest percentage of results (vs draws)',
                    'Most followed cricketer on social media', 'Highest brand value among cricketers']
})

# ===== TAB 1: CAREER OVERVIEW =====
with tab1:
    st.markdown('<div class="subheader-style">Career Highlights</div>', unsafe_allow_html=True)
    
    # Key career stats in 4 columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card"><div class="metric-value">113</div><div class="metric-label">Test Matches</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><div class="metric-value">8,676</div><div class="metric-label">Total Runs</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><div class="metric-value">49.29</div><div class="metric-label">Batting Average</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card"><div class="metric-value">29/29</div><div class="metric-label">100s/50s</div></div>', unsafe_allow_html=True)
    
    # Career timeline
    st.markdown('<div class="subheader-style">Career Timeline</div>', unsafe_allow_html=True)
    
    # Create a yearly runs chart with average overlay
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=yearly_stats['Year'],
        y=yearly_stats['Runs'],
        name='Runs',
        marker_color='#1E3C72'
    ))
    fig.add_trace(go.Scatter(
        x=yearly_stats['Year'],
        y=yearly_stats['Average'],
        name='Average',
        marker_color='#FF4500',
        mode='lines+markers',
        yaxis='y2'
    ))
    fig.update_layout(
        title='Year-wise Performance',
        xaxis_title='Year',
        yaxis_title='Runs',
        yaxis2=dict(
            title='Average',
            overlaying='y',
            side='right'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode="x unified",
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Career phases
    st.markdown('<div class="subheader-style">Career Phases</div>', unsafe_allow_html=True)
    
    # Create a bar chart for different career phases
    fig = px.bar(
        phase_stats,
        x='Phase',
        y='Average',
        text='Average',
        color='Average',
        color_continuous_scale=px.colors.sequential.Blues,
        labels={'Average': 'Batting Average'},
        hover_data=['Period', 'Matches', 'Runs', 'Hundreds', 'Fifties']
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title='Performance in Different Career Phases',
        xaxis_title='Career Phase',
        yaxis_title='Average',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ===== TAB 2: PERFORMANCE ANALYSIS =====
with tab2:
    st.markdown('<div class="subheader-style">Performance Breakdown</div>', unsafe_allow_html=True)
    
    # Two columns for venue and result stats
    col1, col2 = st.columns(2)
    
    with col1:
        # Home vs Away performance
        fig = px.bar(
            venue_stats,
            x='Venue',
            y='Average',
            text='Average',
            color='Venue',
            color_discrete_sequence=['#1E3C72', '#4776E6', '#8E54E9'],
            hover_data=['Matches', 'Runs', 'Hundreds', 'Fifties']
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(
            title='Home vs Away Performance',
            xaxis_title='Venue',
            yaxis_title='Average',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Performance by match result
        fig = px.bar(
            result_stats,
            x='Result',
            y='Average',
            text='Average',
            color='Result',
            color_discrete_sequence=['#4CAF50', '#FF5252', '#FFC107'],
            hover_data=['Matches', 'Runs', 'Hundreds', 'Fifties']
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(
            title='Performance by Match Result',
            xaxis_title='Result',
            yaxis_title='Average',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance against opposition
    st.markdown('<div class="subheader-style">Performance Against Different Opposition</div>', unsafe_allow_html=True)
    
    # Filter out teams with very few matches
    main_opposition = opposition_stats[opposition_stats['Matches'] > 1].copy()
    
    # Create a horizontal bar chart for opposition stats
    fig = px.bar(
        main_opposition.sort_values('Average'),
        y='Opposition',
        x='Average',
        text='Average',
        color='Average',
        orientation='h',
        color_continuous_scale=px.colors.sequential.Blues,
        hover_data=['Matches', 'Runs', 'Hundreds', 'Fifties']
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title='Batting Average Against Different Teams',
        xaxis_title='Average',
        yaxis_title='Opposition',
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Dismissal Pattern
    st.markdown('<div class="subheader-style">Dismissal Pattern Analysis</div>', unsafe_allow_html=True)
    
    # Create pie chart for dismissal types
    fig = px.pie(
        dismissal_pattern,
        values='Percentage',
        names='Dismissal Type',
        color_discrete_sequence=px.colors.sequential.Blues,
        hover_data=['Count', 'Average Before Dismissal']
    )
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(
        title='Dismissal Pattern Breakdown',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ===== TAB 3: CAPTAINCY RECORD =====
with tab3:
    st.markdown('<div class="subheader-style">Captaincy Overview</div>', unsafe_allow_html=True)
    
    # Key captaincy stats in 3 columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><div class="metric-value">68</div><div class="metric-label">Tests as Captain</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><div class="metric-value">40</div><div class="metric-label">Test Wins</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><div class="metric-value">58.8%</div><div class="metric-label">Win Percentage</div></div>', unsafe_allow_html=True)
    
    # Captaincy Venue Record
    st.markdown('<div class="subheader-style">Captaincy Record by Venue</div>', unsafe_allow_html=True)
    
    # Create a grouped bar chart for venue captaincy stats
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=captaincy_venue['Venue'],
        y=captaincy_venue['Won'],
        name='Won',
        marker_color='#4CAF50'
    ))
    fig.add_trace(go.Bar(
        x=captaincy_venue['Venue'],
        y=captaincy_venue['Lost'],
        name='Lost',
        marker_color='#FF5252'
    ))
    fig.add_trace(go.Bar(
        x=captaincy_venue['Venue'],
        y=captaincy_venue['Drawn'],
        name='Drawn',
        marker_color='#FFC107'
    ))
    fig.update_layout(
        barmode='group',
        title='Captaincy Record by Venue',
        xaxis_title='Venue',
        yaxis_title='Number of Matches',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Captaincy Opposition Record
    st.markdown('<div class="subheader-style">Captaincy Record by Opposition</div>', unsafe_allow_html=True)
    
    # Filter teams with more matches
    main_captaincy_opposition = captaincy_opposition[captaincy_opposition['Matches'] >= 4].copy()
    main_captaincy_opposition = main_captaincy_opposition.sort_values('Win %', ascending=False)
    
    # Create a horizontal stacked bar chart
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=main_captaincy_opposition['Opposition'],
        x=main_captaincy_opposition['Won'],
        name='Won',
        orientation='h',
        marker_color='#4CAF50',
        text=main_captaincy_opposition['Won'],
        textposition='auto'
    ))
    fig.add_trace(go.Bar(
        y=main_captaincy_opposition['Opposition'],
        x=main_captaincy_opposition['Lost'],
        name='Lost',
        orientation='h',
        marker_color='#FF5252',
        text=main_captaincy_opposition['Lost'],
        textposition='auto'
    ))
    fig.add_trace(go.Bar(
        y=main_captaincy_opposition['Opposition'],
        x=main_captaincy_opposition['Drawn'],
        name='Drawn',
        orientation='h',
        marker_color='#FFC107',
        text=main_captaincy_opposition['Drawn'],
        textposition='auto'
    ))
    fig.update_layout(
        barmode='stack',
        title='Captaincy Record Against Different Teams',
        xaxis_title='Number of Matches',
        yaxis_title='Opposition',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Batting as captain vs non-captain
    st.markdown('<div class="subheader-style">Batting Performance as Captain</div>', unsafe_allow_html=True)
    
    captain_comparison = pd.DataFrame({
        'Role': ['As Captain', 'Not as Captain'],
        'Average': [54.80, 41.13],
        'Matches': [68, 45],
        'Runs': [5864, 2812],
        'Hundreds': [20, 9],
        'Fifties': [18, 11]
    })
    
    # Create a bar chart for captain vs non-captain
    fig = px.bar(
        captain_comparison,
        x='Role',
        y='Average',
        text='Average',
        color='Role',
        color_discrete_sequence=['#1E3C72', '#4776E6'],
        hover_data=['Matches', 'Runs', 'Hundreds', 'Fifties']
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title='Batting Average: Captain vs Non-Captain',
        xaxis_title='Role',
        yaxis_title='Average',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ===== TAB 4: COMPARATIVE ANALYSIS =====
with tab4:
    st.markdown('<div class="subheader-style">Comparison with Contemporary Batsmen</div>', unsafe_allow_html=True)
    
    # Create a radar chart for contemporary comparison
    categories = ['Tests', 'Average', 'Hundreds', 'Fifties']
    
    fig = go.Figure()
    
    for i, player in enumerate(contemporary_comparison['Batsman']):
        values = [
            contemporary_comparison.loc[i, 'Tests'] / max(contemporary_comparison['Tests']) * 100,
            contemporary_comparison.loc[i, 'Average'] / max(contemporary_comparison['Average']) * 100,
            contemporary_comparison.loc[i, 'Hundreds'] / max(contemporary_comparison['Hundreds']) * 100,
            contemporary_comparison.loc[i, 'Fifties'] / max(contemporary_comparison['Fifties']) * 100
        ]
        # Close the loop
        values.append(values[0])
        categories_with_repeat = categories.copy()
        categories_with_repeat.append(categories[0])
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories_with_repeat,
            fill='toself',
            name=player
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        title="Comparison with Contemporary Batsmen (Normalized %)",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Show raw data in a table
    with st.expander("Show Contemporary Comparison Data"):
        st.dataframe(contemporary_comparison, use_container_width=True)
    
    # Comparison with Indian legends
    st.markdown('<div class="subheader-style">Comparison with Indian Batting Legends</div>', unsafe_allow_html=True)
    
    # Create multiple metrics comparison
    fig = px.scatter(
        indian_legends,
        x='Tests',
        y='Average',
        size='Runs',
        color='Batsman',
        hover_data=['Hundreds', 'Fifties'],
        text='Batsman',
        size_max=60
    )
    fig.update_traces(
        textposition='top center',
        marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey'))
    )
    fig.update_layout(
        title="Indian Batting Legends: Tests vs Average vs Runs",
        xaxis_title="Tests Played",
        yaxis_title="Batting Average",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Show raw data in a table
    with st.expander("Show Indian Legends Comparison Data"):
        st.dataframe(indian_legends, use_container_width=True)

# ===== TAB 5: LEGACY =====
with tab5:
    st.markdown('<div class="subheader-style">Legacy Impact</div>', unsafe_allow_html=True)
    
    # Create a bar chart for legacy impact metrics
    fig = px.bar(
        legacy_impact.sort_values('Score (1-10)', ascending=False),
        y='Impact Area',
        x='Score (1-10)',
        text='Score (1-10)',
        color='Score (1-10)',
        orientation='h',
        color_continuous_scale=px.colors.sequential.Blues,
        hover_data=['Key Evidence']
    )
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(
        title='Legacy Impact Assessment (Score out of 10)',
        xaxis_title='Impact Score',
        yaxis_title='Impact Area',
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Technical Evolution
    st.markdown('<div class="subheader-style">Technical Evolution</div>', unsafe_allow_html=True)
    
    # Create a shot selection evolution chart
    shot_evolution_melted = pd.melt(
        shot_evolution, 
        id_vars=['Shot', 'Effectiveness'], 
        value_vars=['Early Career %', 'Mid Career %', 'Late Career %'],
        var_name='Career Phase', 
        value_name='Percentage'
    )
    
    fig = px.bar(
        shot_evolution_melted,
        x='Shot',
        y='Percentage',
        color='Career Phase',
        barmode='group',
        text='Percentage',
        hover_data=['Effectiveness']
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        title='Shot Selection Evolution Throughout Career',
        xaxis_title='Shot Type',
        yaxis_title='Usage Percentage',
        legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
),
height=500
)
st.plotly_chart(fig, use_container_width=True)

# Display the technical evolution table in an expander
with st.expander("View Technical Evolution Details"):
    st.dataframe(technical_evolution, use_container_width=True)

# Statistical Legacy
st.markdown('<div class="subheader-style">Statistical Legacy</div>', unsafe_allow_html=True)

# Create key achievements in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Key Records & Achievements</h3>
        <ul>
            <li>Most Test wins as Indian captain (40)</li>
            <li>First Asian captain to win a Test series in Australia</li>
            <li>7 double centuries in Test cricket</li>
            <li>Most Test centuries as Indian captain (20)</li>
            <li>Highest Test score: 254* vs South Africa</li>
            <li>Fourth highest century-maker for India in Tests</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Cultural Impact</h3>
        <ul>
            <li>Transformed fitness culture in Indian cricket</li>
            <li>Changed India's approach to fast bowling</li>
            <li>Pioneered aggressive Test captaincy</li>
            <li>Redefined professional standards</li>
            <li>Expanded cricket's global fanbase</li>
            <li>Inspired a generation of young cricketers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Personal insights
st.markdown('<div class="subheader-style">Expert Insights</div>', unsafe_allow_html=True)

expert_quotes = pd.DataFrame({
    'Expert': ['Ravi Shastri (Former Coach)', 'Rahul Dravid (Current Coach)', 'Ian Chappell (Former Australia Captain)', 'Nasser Hussain (Former England Captain)', 'Dale Steyn (South African Fast Bowler)'],
    'Quote': [
        '"Virat Kohli will go down as one of the all-time great captains in world cricket, not just India. His record and legacy speak for themselves."',
        '"His intensity and drive to excel has set new standards for Indian cricket. His legacy goes far beyond numbers."',
        '"Kohli has been the most influential player in Test cricket during his era. His passion for the format helped keep Test cricket alive."',
        '"Kohli changed the face of Indian cricket with his fitness standards and aggressive leadership. India became a team that would not back down."',
        '"The intensity and passion he brings to Test cricket is unmatched. He\'s the batsman I found most challenging to bowl to because he never gives up."'
    ]
})

for i in range(len(expert_quotes)):
    st.markdown(f"""
    <div class="card">
        <i>"{expert_quotes.iloc[i]['Quote']}"</i>
        <br><b>— {expert_quotes.iloc[i]['Expert']}</b>
    </div>
    """, unsafe_allow_html=True)

# Future impact prediction
st.markdown('<div class="subheader-style">Future Impact Projection</div>', unsafe_allow_html=True)

# Create future impact factors
future_impact = pd.DataFrame({
    'Factor': ['Cricket Administration Influence', 'Coaching Potential', 'Media/Commentary Career', 'Cricket Academy Development', 'Global Ambassador Role'],
    'Likelihood (%)': [65, 80, 70, 95, 90],
    'Potential Impact (1-10)': [8, 9, 7, 10, 9]
})

fig = px.scatter(
    future_impact,
    x='Likelihood (%)',
    y='Potential Impact (1-10)',
    text='Factor',
    size='Potential Impact (1-10)',
    color='Likelihood (%)',
    color_continuous_scale=px.colors.sequential.Blues
)
fig.update_traces(
    textposition='top center',
    marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey'))
)
fig.update_layout(
    title="Future Impact Assessment: Likelihood vs Potential Impact",
    xaxis_title="Likelihood (%)",
    yaxis_title="Potential Impact (Scale 1-10)",
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f0f2f6; border-radius: 5px;'>
    <h3>Virat Kohli: Test Cricket Legacy Analysis</h3>
    <p>Data updated as of May 2025 | Created with Streamlit</p>
</div>
""", unsafe_allow_html=True)
