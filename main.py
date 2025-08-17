import crop_diagnosis
import messaging
import voice_query
import localization
import offline_support
import recommendations
import dashboard
import weather

def main():
    # Example usage
    print("Welcome to Mkulima AI!")
    img_path = "sample_crop.jpg"
    result = crop_diagnosis.analyze_image(img_path)
    print(f"Diagnosis: {result}")

    # Weather-based recommendation
    location = "Nairobi"
    weather_info = weather.get_weather(location)
    print(f"Weather update for {location}: {weather_info}")

    smart_reco = recommendations.get_recommendation(result, weather_info)
    print(f"Smart Recommendation: {smart_reco}")

if __name__ == "__main__":
    main()