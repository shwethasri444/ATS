import json

with open('C://Users//admin//heirs//jd_data.json') as jd_data:
    	jds = json.load(jd_data)
    	print(type(jds))
    	jds_string = json.dumps(jds)
    	print(type(jds_string))
    # return render(request, "cupid/profile.html",{"obj_as_json": json.dumps(jds)})