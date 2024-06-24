models = ["Mazda 3",     "Toyota Yaris",     "Volvo S40",    "Mazda 2",  "Toyota Yaris", "Volvo S40"]
colors = ["red",         "white",            "red",          "blue",     "black",        "red"]


# {"Mazda 3": ["red"],
# "Toyota Yaris": ["white", "black"],
# "Volvo S40": ["red"],
# "Mazda 2": ["blue"]}


model_to_colors = {}

# for i in range(len(models)):
#     model = models[i]
#     color = colors[i]

for model, color in zip(models, colors):

    if model not in model_to_colors:
        model_to_colors[model] = {color}
    else:
        model_to_colors[model].add(color)

print(model_to_colors)

# set1 = {1,2,3}
# dict1 = {1:"a", 2:"b"}

# for model in models:
#     print(model)