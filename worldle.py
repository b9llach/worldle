from math import radians, cos, sin, asin, sqrt, floor
import random

def haversine(lat1, lon1, lat2, lon2):
    """
  Calculate the great circle distance in kilometers between two points
  on the earth (specified in decimal degrees)
  """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956
    return c * r

countries = [
    {"name": "Afghanistan", "lat": 33, "long": 66, "pic": "imgs/af-512.png"},
    {"name": "Albania", "lat": 41, "long": 20, "pic": "imgs/al-512.png"},
    {"name": "Algeria", "lat": 28, "long": 3, "pic": "imgs/af-512.png"},
    {"name": "Andorra", "lat": 42.5, "long": 1.5},
    {"name": "Angola", "lat": -12.5, "long": 18.5},
    {"name": "Antigua and Barbuda", "lat": 17.05, "long": -61.8},
    {"name": "Argentina", "lat": -34, "long": -64},
    {"name": "Armenia", "lat": 40, "long": 45},
    {"name": "Australia", "lat": -25, "long": 135},
    {"name": "Austria", "lat": 47.333333, "long": 13.333333},
    {"name": "Azerbaijan", "lat": 40.5, "long": 47.5},
    {"name": "Bahamas", "lat": 24, "long": -76},
    {"name": "Bahrain", "lat": 26, "long": 50.5},
    {"name": "Bangladesh", "lat": 24, "long": 90},
    {"name": "Barbados", "lat": 13.166667, "long": -59.533333},
    {"name": "Belarus", "lat": 53, "long": 28},
    {"name": "Belgium", "lat": 50.833333, "long": 4},
    {"name": "Belize", "lat": 17.25, "long": -88.75},
    {"name": "Benin", "lat": 9.5, "long": 2.25},
    {"name": "Bhutan", "lat": 27.5, "long": 90.5},
    {"name": "Bolivia", "lat": -17, "long": -65},
    {"name": "Bosnia and Herzegovina", "lat": 44.25, "long": 17.833333},
    {"name": "Botswana", "lat": -22, "long": 24},
    {"name": "Brazil", "lat": -10, "long": -55},
    {"name": "Brunei Darussalam", "lat": 4.5, "long": 114.666667},
    {"name": "Bulgaria", "lat": 43, "long": 25},
    {"name": "Burkina Faso", "lat": 13, "long": -2},
    {"name": "Burundi", "lat": -3.5, "long": 30},
    {"name": "Cabo Verde", "lat": 16, "long": -24},
    {"name": "Cambodia", "lat": 13, "long": 105},
    {"name": "Cameroon", "lat": 6, "long": 12},
    {"name": "Canada", "lat": 60, "long": -96},
    {"name": "Central African Republic", "lat": 7, "long": 21},
    {"name": "Chad", "lat": 15, "long": 19},
    {"name": "Chile", "lat": -30, "long": -71},
    {"name": "China", "lat": 35, "long": 105},
    {"name": "Colombia", "lat": 4, "long": -72},
    {"name": "Comoros", "lat": -12.166667, "long": 44.25},
    {"name": "Congo", "lat": -1, "long": 15},
    {"name": "Costa Rica", "lat": 10, "long": -84},
    {"name": "Ivory Coast", "lat": 8, "long": -5},
    {"name": "Croatia", "lat": 45.166667, "long": 15.5},
    {"name": "Cuba", "lat": 22, "long": -79.5},
    {"name": "Cyprus", "lat": 35, "long": 33},
    {"name": "Czech Republic", "lat": 49.75, "long": 15},
    {"name": "Democratic People’s Republic of Korea", "lat": 40, "long": 127},
    {"name": "Democratic Republic of the Congo", "lat": 0, "long": 25},
    {"name": "Denmark", "lat": 56, "long": 10},
    {"name": "Djibouti", "lat": 11.5, "long": 42.5},
    {"name": "Dominica", "lat": 15.5, "long": -61.333333},
    {"name": "Dominican Republic", "lat": 19, "long": -70.666667},
    {"name": "Ecuador", "lat": -2, "long": -77.5},
    {"name": "Egypt", "lat": 27, "long": 30},
    {"name": "El Salvador", "lat": 13.833333, "long": -88.916667},
    {"name": "Equatorial Guinea", "lat": 2, "long": 10},
    {"name": "Eritrea", "lat": 15, "long": 39},
    {"name": "Estonia", "lat": 59, "long": 26},
    {"name": "Ethiopia", "lat": 8, "long": 38},
    {"name": "Fiji", "lat": -18, "long": 178},
    {"name": "Finland", "lat": 64, "long": 26},
    {"name": "France", "lat": 46, "long": 2},
    {"name": "Gabon", "lat": -1, "long": 11.75},
    {"name": "Gambia", "lat": 13.5, "long": -15.5},
    {"name": "Georgia", "lat": 41.999981, "long": 43.499905},
    {"name": "Germany", "lat": 51.5, "long": 10.5},
    {"name": "Ghana", "lat": 8, "long": -2},
    {"name": "Greece", "lat": 39, "long": 22},
    {"name": "Grenada", "lat": 12.116667, "long": -61.666667},
    {"name": "Guatemala", "lat": 15.5, "long": -90.25},
    {"name": "Guinea", "lat": 11, "long": -10},
    {"name": "Guinea-Bissau", "lat": 12, "long": -15},
    {"name": "Guyana", "lat": 5, "long": -59},
    {"name": "Haiti", "lat": 19, "long": -72.416667},
    {"name": "Honduras", "lat": 15, "long": -86.5},
    {"name": "Hungary", "lat": 47, "long": 20},
    {"name": "Iceland", "lat": 65, "long": -18},
    {"name": "India", "lat": 20, "long": 77},
    {"name": "Indonesia", "lat": -5, "long": 120},
    {"name": "Iran", "lat": 32, "long": 53},
    {"name": "Iraq", "lat": 33, "long": 44},
    {"name": "Ireland", "lat": 53, "long": -8},
    {"name": "Israel", "lat": 31.5, "long": 34.75},
    {"name": "Italy", "lat": 42.833333, "long": 12.833333},
    {"name": "Jamaica", "lat": 18.25, "long": -77.5},
    {"name": "Japan", "lat": 36, "long": 138},
    {"name": "Jordan", "lat": 31, "long": 36},
    {"name": "Kazakhstan", "lat": 48, "long": 68},
    {"name": "Kenya", "lat": 1, "long": 38},
    {"name": "Kiribati", "lat": -5, "long": -170},
    {"name": "Kuwait", "lat": 29.5, "long": 47.75},
    {"name": "Kyrgyzstan", "lat": 41, "long": 75},
    {"name": "Laos", "lat": 18, "long": 105},
    {"name": "Latvia", "lat": 57, "long": 25},
    {"name": "Lebanon", "lat": 33.833333, "long": 35.833333},
    {"name": "Lesotho", "lat": -29.5, "long": 28.25},
    {"name": "Liberia", "lat": 6.5, "long": 9.5},
    {"name": "Libya", "lat": 25, "long": 17},
    {"name": "Liechtenstein", "lat": 47.166667, "long": 9.533333},
    {"name": "Lithuania", "lat": 56, "long": 24},
    {"name": "Luxembourg", "lat": 49.75, "long": 6.166667},
    {"name": "Macedonia", "lat": 41.833333, "long": 22},
    {"name": "Madagascar", "lat": -20, "long": 47},
    {"name": "Malawi", "lat": -13.5, "long": 34},
    {"name": "Malaysia", "lat": 2.5, "long": 112.5},
    {"name": "Maldives", "lat": 3.2, "long": 73},
    {"name": "Mali", "lat": 17, "long": -4},
    {"name": "Malta", "lat": 35.916667, "long": 14.433333},
    {"name": "Marshall Islands", "lat": 10, "long": 167},
    {"name": "Mauritania", "lat": 20, "long": -12},
    {"name": "Mauritius", "lat": -20.3, "long": 57.583333},
    {"name": "Mexico", "lat": 23, "long": -102},
    {"name": "Federated States of Micronesia", "lat": 5, "long": 152},
    {"name": "Monaco", "lat": 43.733333, "long": 7.4},
    {"name": "Mongolia", "lat": 46, "long": 105},
    {"name": "Montenegro", "lat": 42.5, "long": 19.3},
    {"name": "Morocco", "lat": 32, "long": -5},
    {"name": "Mozambique", "lat": -18.25, "long": 35},
    {"name": "Myanmar", "lat": 22, "long": 98},
    {"name": "Namibia", "lat": -22, "long": 17},
    {"name": "Nauru", "lat": -0.533333, "long": 166.916667},
    {"name": "Nepal", "lat": 28, "long": 84},
    {"name": "Netherlands", "lat": 52.5, "long": 5.75},
    {"name": "New Zealand", "lat": -42, "long": 174},
    {"name": "Nicaragua", "lat": 13, "long": -85},
    {"name": "Niger", "lat": 16, "long": 8},
    {"name": "Nigeria", "lat": 10, "long": 8},
    {"name": "Norway", "lat": 62, "long": 10},
    {"name": "Oman", "lat": 21, "long": 57},
    {"name": "Pakistan", "lat": 30, "long": 70},
    {"name": "Palau", "lat": 6, "long": 134},
    {"name": "Panama", "lat": 9, "long": -80},
    {"name": "Papua New Guinea", "lat": -6, "long": 147},
    {"name": "Paraguay", "lat": -22.993333, "long": -57.996389},
    {"name": "Peru", "lat": -10, "long": -76},
    {"name": "Philippines", "lat": 13, "long": 122},
    {"name": "Poland", "lat": 52, "long": 20},
    {"name": "Portugal", "lat": 39.5, "long": -8},
    {"name": "Qatar", "lat": 25.5, "long": 51.25},
    {"name": "Republic of Korea", "lat": 37, "long": 127.5},
    {"name": "Republic of Moldova", "lat": 47, "long": 29},
    {"name": "Romania", "lat": 46, "long": 25},
    {"name": "Russian Federation", "lat": 60, "long": 100},
    {"name": "Rwanda", "lat": -2, "long": 30},
    {"name": "Saint Kitts and Nevis", "lat": 17.333333, "long": -62.75},
    {"name": "Saint Lucia", "lat": 13.883333, "long": -60.966667},
    {"name": "Saint Vincent and the Grenadines", "lat": 13.083333, "long": -61.2},
    {"name": "Samoa", "lat": -13.803096, "long": -172.178309},
    {"name": "San Marino", "lat": 43.933333, "long": 12.416667},
    {"name": "Sao Tome and Principe", "lat": 1, "long": 7},
    {"name": "Saudi Arabia", "lat": 25, "long": 45},
    {"name": "Senegal", "lat": 14, "long": -14},
    {"name": "Serbia", "lat": 44, "long": 21},
    {"name": "Seychelles", "lat": -4.583333, "long": 55.666667},
    {"name": "Sierra Leone", "lat": 8.5, "long": -11.5},
    {"name": "Singapore", "lat": 1.366667, "long": 103.8},
    {"name": "Slovakia", "lat": 48.666667, "long": 19.5},
    {"name": "Slovenia", "lat": 46.25, "long": 15.166667},
    {"name": "Solomon Islands", "lat": -8, "long": 159},
    {"name": "Somalia", "lat": 6, "long": 48},
    {"name": "South Africa", "lat": -30, "long": 26},
    {"name": "South Sudan", "lat": 8, "long": 30},
    {"name": "Spain", "lat": 40, "long": -4},
    {"name": "Sri Lanka", "lat": 7, "long": 81},
    {"name": "Sudan", "lat": 16, "long": 30},
    {"name": "Suriname", "lat": 4, "long": -56},
    {"name": "Swaziland", "lat": -26.5, "long": 31.5},
    {"name": "Sweden", "lat": 62, "long": 15},
    {"name": "Switzerland", "lat": 47, "long": 8},
    {"name": "Syrian Arab Republic", "lat": 35, "long": 38},
    {"name": "Tajikistan", "lat": 39, "long": 71},
    {"name": "Tanzania", "lat": -6, "long": 35},
    {"name": "Thailand", "lat": 15, "long": 100},
    {"name": "Timor-Leste", "lat": -8.833333, "long": 125.75},
    {"name": "Togo", "lat": 8, "long": 1.166667},
    {"name": "Tonga", "lat": -20, "long": -175},
    {"name": "Trinidad and Tobago", "lat": 11, "long": -61},
    {"name": "Tunisia", "lat": 34, "long": 9},
    {"name": "Turkey", "lat": 39.059012, "long": 34.911546},
    {"name": "Turkmenistan", "lat": 40, "long": 60},
    {"name": "Tuvalu", "lat": -8, "long": 178},
    {"name": "Uganda", "lat": 2, "long": 33},
    {"name": "Ukraine", "lat": 49, "long": 32},
    {"name": "United Arab Emirates", "lat": 24, "long": 54},
    {"name": "United Kingdom", "lat": 54, "long": -4},
    {"name": "United States of America", "lat": 39.828175, "long": -98.5795},
    {"name": "Uruguay", "lat": -33, "long": -56},
    {"name": "Uzbekistan", "lat": 41.707542, "long": 63.84911},
    {"name": "Vanuatu", "lat": -16, "long": 167},
    {"name": "Venezuela", "lat": 8, "long": -66},
    {"name": "Vietnam", "lat": 16.166667, "long": 107.833333},
    {"name": "Yemen", "lat": 15.5, "long": 47.5},
    {"name": "Zambia", "lat": -15, "long": 30},
    {"name": "Zimbabwe", "lat": -19, "long": 29}
]


class Worldle:
    ccountry = {}

    def get_country(self) -> None:
        # global ccountry
        r = random.randrange(0, len(countries))
        self.ccountry = {"name": countries[r]["name"], "lat": countries[r]["lat"], "long": countries[r]["long"]}

    def get_distance(self, gcountry: str) -> dict:
        for i in countries:
            if i["name"].lower() == gcountry.lower():
                guess = (i["lat"], i["long"])
                actual = (self.ccountry["lat"], self.ccountry["long"])
                dist = haversine(guess[0], guess[1], actual[0], actual[1])
                return {"distance": int(dist), "direction": self.get_direction(guess, actual),
                        "percentage": 100 - floor(dist / 24901 * 100)}
        return {"distance": "N/A", "direction": "N/A", "percentage": "N/A"}

    def get_direction(self, guess: tuple, actual: tuple) -> str:
        direction = ""
        if actual[0] > guess[0]:
            direction = "North"
            if actual[1] > guess[1]:
                direction = "North East"
            elif actual[1] < guess[1]:
                direction = "North West"

        elif guess[0] > actual[0]:
            direction = "South"
            if actual[1] > guess[1]:
                direction = "South East"
            elif actual[1] < guess[1]:
                direction = "South West"

        else:
            direction = "Perfect"

        return direction

    def game_loop(self):
        while True:
            attempts = 0
            self.get_country()
            guesses = []
            while attempts < 6:
                valid_guess = False
                while not valid_guess:
                    guess = input("\nGuess a country: ")
                    rt = self.get_distance(guess)
                    if rt["distance"] != "N/A":

                        if rt["distance"] == 0:
                            guesses.append(f"{guess.title()} was correct | {rt['percentage']}% | {rt['direction']}\n")
                            for i in guesses:
                                print(i)
                            self.game_loop()

                        guesses.append(f"{guess.title()} | {rt['percentage']}% | {rt['distance']} Miles {rt['direction']}")
                        valid_guess = True
                        attempts += 1
                        for i in guesses:
                            print(i)
                        if attempts == 5:
                            print(f"Out of attempts. The country was {self.ccountry['name']}")







