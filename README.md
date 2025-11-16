# GPSi - GPS intelegent predicts risks 

## Project Overview
This project is an **Intelligent GPS system** designed to **warn drivers about potentially dangerous roads** before they travel them. Roads with risks such as slippery conditions, high accident history, or other hazards will be highlighted, and safer alternative routes will be suggested.

**Current Demo:**  
The current version is a **prototype/demo** that shows hazard markers on an interactive dark-themed map centered on Tunisia.  

**Future AI Integration:**  
We plan to implement AI to predict road hazards in real-time and provide dynamic route suggestions based on:  
- Historical accident data  
- Road conditions and weather data  
- Traffic patterns  

---

## How AI Will Be Used
1. **Data Collection:**  
   - Public datasets of road accidents, traffic, and weather in Tunisia and nearby regions  
   - OpenStreetMap data for road networks and attributes  
   - Optional crowd-sourced reports from drivers (for real-time updates)  

2. **Model Training:**  
   - Use Python, TensorFlow, or PyTorch  
   - Train models to classify roads by risk level based on historical and real-time data  

3. **Prediction and Suggestion:**  
   - The AI model will predict risk scores for upcoming routes  
   - Suggest alternative safer routes if high-risk roads are detected  

---

## Demo Features
- Interactive dark-mode map with colored risk markers:  
  - **Red**: High risk  
  - **Orange**: Medium risk  
  - **Green**: Low risk  
- Popups for each road showing: name, risk level, reason, and suggested alternative  
- Floating legend for quick understanding of risks  

---

## Technologies
- **Frontend:** HTML, CSS, JavaScript  
- **Map:** [Leaflet.js](https://leafletjs.com/) with Carto Dark tiles  
- **Backend :** Flask to serve dynamic data  
- **AI (planned):** Python, TensorFlow/PyTorch, Pandas, NumPy, scikit-learn  

