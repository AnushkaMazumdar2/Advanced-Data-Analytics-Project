import pandas as pd

# Manually create the dataset as a list of dictionaries
data = [
    {
        "Year": 2014,
        "City": "Ahmedabad",
        "Population(in lakhs)": 69.5,
        "Murder": 82,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2015,
        "City": "Ahmedabad",
        "Population(in lakhs)": 71.1,
        "Murder": 94,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2016,
        "City": "Ahmedabad",
        "Population(in lakhs)": 72.3,
        "Murder": 103,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2017,
        "City": "Ahmedabad",
        "Population(in lakhs)": 74.9,
        "Murder": 90,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },{
        "Year": 2018,
        "City": "Ahmedabad",
        "Population(in lakhs)": 76.8,
        "Murder": 98,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },{
        "Year": 2019,
        "City": "Ahmedabad",
        "Population(in lakhs)": 78.7,
        "Murder": 81,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },{
        "Year": 2020,
        "City": "Ahmedabad",
        "Population(in lakhs)": 80.6,
        "Murder": 70,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2021,
        "City": "Ahmedabad",
        "Population(in lakhs)": 82.5,
        "Murder": 97,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2022,
        "City": "Ahmedabad",
        "Population(in lakhs)": 84.5,
        "Murder": 82,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2023,
        "City": "Ahmedabad",
        "Population(in lakhs)": 86.5,
        "Murder": 82,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
    {
        "Year": 2024,
        "City": "Ahmedabad",
        "Population(in lakhs)": 88.5,
        "Murder": 82,
        "Kidnapping": 367,
        "Crime against women": 1371,
        "Crime against children": 437,
        "Crime committed by juveniles": 215,
        "crime against senior citizen": 68,
        "crime against sc": 66,
        "crime against ST": 6,
        "Economic Offences": 399,
        "Cyber Crimes": 32
    },
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = "crp.xlsx"
df.to_excel(output_file, index=False)

print(f"Data successfully created and saved to {output_file}")
