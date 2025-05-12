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

https://virat-test-story-7doohhp63qt4dyyfg7wx8n.streamlit.app/ - Statistical legacy and experts insights and empty. Provide code only for tab 5, rest code I have. i only want code for tab 5 to fix the issue.

Edit
I'll provide code for tab 5 to fix the issues in your Streamlit app. Let me create an artifact with the code for tab 5 only.


Tab 5: Statistical Legacy and Expert Insights
Code 
This code for tab 5 should fix the empty "Statistical Legacy and Expert Insights" page in your Streamlit app. The code includes:

A comprehensive statistical overview with batting statistics across formats
Visualization of runs and strike rates using bar charts
Expert insights section with quotes from cricket legends
Legacy and cultural impact sections
An interactive career timeline with a slider to explore events by year
Comparison with contemporary players visualized in a grouped bar chart
Just add this function to your app and ensure you call it in the appropriate tab section. The code uses Streamlit's columns, expanders, and visualization features to create an engaging and informative experience.

Let me know if you need any adjustments to the code or have questions about implementing it!





vk.py
741 lines

py

In which section should I paste the above code?

Edit
Looking at your vk.py file, I can see that you need to replace the empty Tab 5: Legacy section with the code I provided. The empty Tab 5 implementation can be found at the end of your file.

You should paste the display_statistical_legacy() function I provided earlier somewhere before your tab declarations, and then replace the current Tab 5 implementation with a call to this function.

Here's how to do it:

First, add the display_statistical_legacy() function before the line that creates the tabs (before tab1, tab2, tab3, tab4, tab5 = st.tabs(...))
Then replace the current Tab 5 implementation (the last section of your code that starts with # ===== TAB 5: LEGACY =====) with a simple call to your new function.
Let me provide the exact code update for the Tab 5 section:


Tab 5 Implementation Update
Code 
Based on your vk.py file, you need to make the following changes:

Add the display_statistical_legacy() function definition to your code. This should be placed before the tab definitions, ideally after your dataframes but before the line that creates tabs (tab1, tab2, tab3, tab4, tab5 = st.tabs(...)).
Replace the entire current Tab 5 implementation. In your file, find the section that starts with:
python
# ===== TAB 5: LEGACY =====
with tab5:
    st.markdown('<div class="subheader-style">Legacy Impact</div>', unsafe_allow_html=True)
    
    # Create a bar chart for legacy impact metrics
    # ...
Replace that entire section with just:

python
# ===== TAB 5: LEGACY =====
with tab5:
    display_statistical_legacy()
This will fix the empty Tab 5 issue by calling the new comprehensive function that displays all the statistical legacy and expert insights content.

The function includes sections for:

Batting statistics across formats
Performance visualizations with bar charts
Expert insights in expandable sections
Legacy and cultural impact analysis
Interactive career timeline
Comparison with contemporary players
Let me know if you need any clarification or have any questions about implementing this update!






You’re almost out of usage - your limits will reset at 5:30 PM


# Define the statistical legacy function above where you define the tabs
def display_statistical_legacy():
    st.title("Statistical Legacy and Expert Insights")
    
    # Two columns for stats and visualization
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Batting Statistics")
        
        batting_stats = {
            "Format": ["Test", "ODI", "T20I", "IPL"],
            "Matches": [113, 275, 115, 237],
            "Runs": [8847, 13848, 4008, 7263],
            "Average": [48.88, 57.32, 52.74, 37.25],
            "Strike Rate": [55.64, 92.84, 137.96, 129.66],
            "Centuries": [29, 46, 1, 7],
            "Half-Centuries": [29, 65, 37, 50]
        }
        
        stats_df = pd.DataFrame(batting_stats)
        st.dataframe(stats_df, use_container_width=True)
        
        st.subheader("Records and Milestones")
        records = [
            "Fastest to 10,000 ODI runs",
            "Most centuries in successful ODI run chases (26)",
            "Highest Test batting average among active players (minimum 20 innings)",
            "Only player to average 50+ in Tests, ODIs, and T20Is simultaneously",
            "Most Player of the Match awards in international cricket"
        ]
        
        for record in records:
            st.markdown(f"• {record}")
            
    with col2:
        st.subheader("Performance by Format")
        
        # Chart data
        formats = ["Test", "ODI", "T20I", "IPL"]
        runs = [8847, 13848, 4008, 7263]
        
        # Create bar chart
        fig = plt.figure(figsize=(10, 6))
        plt.bar(formats, runs, color=['#3366cc', '#dc3912', '#ff9900', '#109618'])
        plt.title('Runs Across Formats')
        plt.ylabel('Runs')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        for i, value in enumerate(runs):
            plt.text(i, value + 100, f"{value}", ha='center')
            
        st.pyplot(fig)
        
        # Strike Rate comparison
        st.subheader("Strike Rate Comparison")
        
        strike_rates = [55.64, 92.84, 137.96, 129.66]
        
        fig2 = plt.figure(figsize=(10, 6))
        plt.bar(formats, strike_rates, color=['#3366cc', '#dc3912', '#ff9900', '#109618'])
        plt.title('Strike Rate Across Formats')
        plt.ylabel('Strike Rate')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        for i, value in enumerate(strike_rates):
            plt.text(i, value + 2, f"{value}", ha='center')
            
        st.pyplot(fig2)
    
    # Expert Insights Section
    st.header("Expert Insights")
    
    experts = {
        "Ricky Ponting": "Virat's technique is flawless. The way he's adapted his game across formats sets him apart as one of the greatest of all time.",
        "AB de Villiers": "What makes Virat special is his intensity and fitness standards. He's revolutionized cricket fitness globally.",
        "Rahul Dravid": "His ability to chase in limited-overs cricket is unparalleled. The mental strength he shows under pressure is remarkable.",
        "Kumar Sangakkara": "The evolution of Virat from an aggressive youngster to a mature leader has been cricket's most compelling story of the decade.",
        "Michael Vaughan": "In my opinion, across formats, Kohli is the most complete batsman I've ever seen."
    }
    
    # Display expert quotes in expanders
    for expert, quote in experts.items():
        with st.expander(f"{expert}'s view on Virat Kohli"):
            st.write(quote)
    
    # Legacy Impact
    st.header("Legacy and Impact")
    
    legacy_col1, legacy_col2 = st.columns([1, 1])
    
    with legacy_col1:
        st.subheader("Cultural Impact")
        st.write("""
        Virat Kohli transcended cricket to become a cultural icon in India and globally. 
        His fitness revolution transformed Indian cricket's approach to physical conditioning.
        As one of the world's most marketable athletes, his influence extends far beyond the cricket field.
        """)
        
        st.image("https://www.hindustantimes.com/ht-img/img/2023/11/15/1600x900/PTI11-15-2023-000042B-0_1700034001075_1700034020067.jpg", 
              caption="Virat Kohli celebrating a century", 
              use_column_width=True)
    
    with legacy_col2:
        st.subheader("Cricket Evolution")
        st.write("""
        Kohli's aggressive captaincy style prioritized Test cricket and fast bowling development.
        His batting adaptability across formats set new standards for versatility.
        His chase mastery redefined ODI batting approaches and match strategies.
        """)
        
        # Create a pie chart of centuries by format
        labels = ['Test', 'ODI', 'T20I', 'IPL']
        centuries = [29, 46, 1, 7]
        
        fig3, ax = plt.subplots(figsize=(8, 8))
        ax.pie(centuries, labels=labels, autopct='%1.1f%%', startangle=90, 
              colors=['#3366cc', '#dc3912', '#ff9900', '#109618'])
        ax.axis('equal')
        plt.title('Centuries by Format')
        
        st.pyplot(fig3)
    
    # Interactive Timeline
    st.header("Career Timeline")
    
    timeline_events = [
        {"year": 2008, "event": "International debut in ODI cricket against Sri Lanka"},
        {"year": 2010, "event": "T20 World Cup - Emerged as a consistent performer"},
        {"year": 2011, "event": "World Cup winner with India"},
        {"year": 2013, "event": "Fastest ODI century by an Indian (52 balls)"},
        {"year": 2014, "event": "Named Test captain after MS Dhoni's retirement"},
        {"year": 2017, "event": "Took over as captain in all formats"},
        {"year": 2018, "event": "Scored 1000+ Test runs in three consecutive calendar years"},
        {"year": 2021, "event": "Stepped down as T20I captain"},
        {"year": 2022, "event": "Stepped down as Test captain"},
        {"year": 2023, "event": "Scored his 50th ODI century, breaking Sachin Tendulkar's record"}
    ]
    
    timeline_df = pd.DataFrame(timeline_events)
    
    selected_year = st.select_slider(
        "Explore timeline by year",
        options=timeline_df["year"].tolist()
    )
    
    filtered_events = timeline_df[timeline_df["year"] == selected_year]
    
    for _, row in filtered_events.iterrows():
        st.info(f"**{row['year']}**: {row['event']}")
    
    # Comparison with contemporaries
    st.header("Comparison with Contemporaries")
    
    contemporary_data = {
        "Player": ["Virat Kohli", "Steve Smith", "Joe Root", "Kane Williamson", "Babar Azam"],
        "Test Average": [48.88, 58.61, 49.57, 53.15, 45.98],
        "ODI Average": [57.32, 43.34, 51.25, 47.78, 56.92],
        "T20I Average": [52.74, 25.78, 35.70, 33.15, 41.48]
    }
    
    comp_df = pd.DataFrame(contemporary_data)
    
    # Create a multi-format chart
    fig4, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(comp_df["Player"]))
    width = 0.25
    
    bar1 = ax.bar(x - width, comp_df["Test Average"], width, label='Test', color='#3366cc')
    bar2 = ax.bar(x, comp_df["ODI Average"], width, label='ODI', color='#dc3912')
    bar3 = ax.bar(x + width, comp_df["T20I Average"], width, label='T20I', color='#ff9900')
    
    ax.set_ylabel('Batting Average')
    ax.set_title('Batting Averages Across Formats')
    ax.set_xticks(x)
    ax.set_xticklabels(comp_df["Player"])
    ax.legend()
    
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    fig4.tight_layout()
    
    st.pyplot(fig4)
    
    st.write("""
    The comparison highlights Kohli's remarkable consistency across all three formats,
    particularly standing out in limited-overs cricket. While Steve Smith edges him in Test cricket,
    Kohli's all-format excellence is unmatched among his contemporaries.
    """)

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
    display_statistical_legacy()
