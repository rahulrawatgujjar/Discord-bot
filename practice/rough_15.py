# from prsaw import RandomStuffV4
# rs=RandomStuffV4(api_key="********")
# que=input()
# response=rs.get_ai_response(que,unique_id="****************")
# print(response)
# rs.close()


import requests
question=input()
url = "https://random-stuff-api.p.rapidapi.com/ai"

# querystring = {"msg":f"{question}","bot_name":"Random Stuff Api (OPTIONAL)","bot_gender":"male (OPTIONAL)","bot_master":"PGamerX (OPTIONAL)","bot_age":"19 (OPTIONAL)","bot_company":"PGamerX Studio (OPTIONAL)","bot_location":"India (OPTIONAL)","bot_email":"admin@pgamerx.com (OPTIONAL)","bot_build":"Public (OPTIONAL)","bot_birth_year":"2002 (OPTIONAL)","bot_birth_date":"1st January, 2002 (OPTIONAL)","bot_birth_place":"India (OPTIONAL)","bot_favorite_color":"Blue (OPTIONAL)","bot_favorite_book":"Harry Potter (OPTIONAL)","bot_favorite_band":"Imagine Doggos (OPTIONAL)","bot_favorite_artist":"Eminem (OPTIONAL)","bot_favorite_actress":"Emma Watson (OPTIONAL)","bot_favorite_actor":"Jim Carrey (OPTIONAL)","id":"For customised response for each user"}
querystring={"msg":f"{question}"}

headers = {
	"Authorization": "*****",
	"X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com",
	"X-RapidAPI-Key": "******************"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
ind=response.text.index("AIResponse")+13
print(response.text[ind:-1])
# print(response.text["AIResponse"])
