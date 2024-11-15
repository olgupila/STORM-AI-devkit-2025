# Background

<div style="display: flex; flex-direction: column; background-color: #f9f9f9; border-left: 6px solid #ff4d00; border-radius: 4px; padding: 15px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff; background-color: #ff4d00; display: inline-block; padding: 5px 10px; border-radius: 3px; margin-bottom: 10px;">⚠️ Attention</div>
    <p style="font-size: 14px; margin: 0; color: #555;"> This approach is <strong>NOT a challenge baseline</strong>. A <strong>baseline solution</strong>, detailing exactly what we expect you to provide, will be made available to participants on <u>December 16, 2024</u>.</strong>.</p>
</div>

Here we present some of the approaches already developed to forecast atmospheric density, aiming to improve satellite drag prediction and orbit propagation. The models trained in this context provide valuable insights into handling space weather data to derive atmospheric density. These models utilize solar and geomagnetic indices, such as solar flux and geomagnetic activity, along with temporal features derived from sliding windows that capture historical and contextual patterns. By leveraging advanced architectures like transformers and reduced-order models (ROM), these models learn the intricate relationships between solar and geomagnetic activities and their impact on atmospheric density. Once trained, they generate forecasts of atmospheric density at various altitudes and locations, predictions that are essential for satellite orbit propagation, drag estimation, and collision avoidance, thereby enhancing the safety and efficiency of space operations.

This approach forms the foundation of this challenge but is not the exact task participants are required to perform. However, participants can draw insights from this solution. It serves as a baseline for assessing more advanced AI solutions and helps participants become familiar with the dataset, methodologies, and evaluation pipeline. For those new to the field, the baseline implementation provides a solid starting point, allowing for iterative improvements and experimentation with newer AI techniques. We encourage you to explore [the model this competition is inspired by](https://github.com/ARCLab-MIT/2025-aichallenge-devkit/tree/main/background_model) to gain a deeper understanding of the atmospheric density forecasting problem.

Using the approach outlined, you can generate atmospheric density information as follows: NRLMSIS 2.0, an empirical atmospheric density model, requires satellite time, altitude, longitude, latitude, and two additional space weather parameters: F10.7 solar flux and Ap geomagnetic index. These parameters are sourced from NASA's historical [OMNI dataset](https://omniweb.gsfc.nasa.gov/). The [pymsis](https://pypi.org/project/pymsis/) package is then used to generate atmospheric density values along an expected satellite orbit.




