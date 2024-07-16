Youth Baseball League IoT Decision-Making Application

Overview

This project centers around an IoT application developed using Raspberry Pi and Sense HAT to aid youth baseball league conveners in making weather-dependent decisions. The application provides real-time guidance on whether games should proceed, be postponed, or canceled based on player age and weather conditions fetched from the OpenWeatherMap API.
Key Features

    Real-time Decision Support: Utilizes OpenWeatherMap API to gather temperature and weather information, focusing on conditions like thunderstorms or rain which can impact gameplay safety and quality.

    Visual Indicators: The Sense HAT display offers immediate visual feedback:
        NO-GO (Flashing Red X): Indicates unsuitable playing conditions, prompting game postponement or cancellation.
        GO (Green Checkmark): Signals acceptable conditions for gameplay.

    Age-Specific Decision Logic:
        For players under 16 years old, the application prioritizes safety concerns and parental considerations.
        Older players, more independent in travel, may proceed with games under certain weather conditions.

Implementation Details

    Hardware: Each baseball diamond is equipped with a Raspberry Pi connected to a Sense HAT for real-time weather monitoring and display updates.

    Software: Python script integrates with OpenWeatherMap API:
        Retrieves current weather conditions and temperature data.
        Analyzes weather conditions against predefined thresholds (e.g., thunderstorms, rain intensity).
        Updates the Sense HAT display with appropriate visual indicators based on weather and player age.

Decision Making Process

    Weather Data Retrieval: The application fetches real-time weather updates from OpenWeatherMap API, focusing on conditions impacting gameplay safety.

    Player Age Analysis: The system differentiates between younger and older player groups to tailor decision-making.

    Display Logic:
        If weather conditions indicate thunderstorms or rain and players are under 16, display a flashing red X indicating NO-GO.
        If conditions are favorable or players are older than 16, display a green checkmark signaling GO.

Benefits

    Enhanced Safety: Utilizes real-time weather data to prioritize player safety and well-being during games.

    Efficient Decision-Making: Automates game status updates based on weather conditions, reducing manual intervention.

    Improved Transparency: Provides clear communication to parents and players regarding game status, ensuring a positive league experience.


Conclusion

This IoT application exemplifies the integration of technology in managing youth sports, specifically in youth baseball leagues. By leveraging Raspberry Pi and Sense HAT capabilities along with real-time weather data from OpenWeatherMap API, the project showcases how IoT can streamline decision-making processes, ensuring safety and operational efficiency in sports management.