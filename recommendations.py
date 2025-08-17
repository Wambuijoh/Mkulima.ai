# Smart recommendations with weather context
def get_recommendation(diagnosis, weather):
    if diagnosis == "Early blight detected":
        if weather and "humidity" in weather and weather["humidity"] > 80:
            return "Apply fungicide, monitor due to high humidity risk."
        else:
            return "Apply fungicide and monitor crops."
    return "No action needed."