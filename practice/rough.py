# import the module
import python_weather
import asyncio

async def getweather(city):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)
    print(weather.current.sky_text)
    print(weather.current.date)

    # # get the weather forecast for a few days
    # for forecast in weather.forecasts:
    #     print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()
    return weather.current.sky_text
    # await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    city="bhiwani"
    r=loop.run_until_complete(getweather(city))
    print(r)
    
    