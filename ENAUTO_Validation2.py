
return_val = {
    "alertData":{
        "countNode":1,
        "bssids": [
            "aa:bb",
            "22:33"
        ],
        "min":123,
        "max":12312
    },
    "alertID":1231312313
}

# bssids =return_val["alertData"]["bssids"]
# for value in bssids:
#     print("ALERT: lalala - "+value)


print(return_val["alertData"]["min"])
