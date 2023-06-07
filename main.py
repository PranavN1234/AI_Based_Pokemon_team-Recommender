
import openai
import requests
import Levenshtein

def getExactMatch(target, pokemon_names):

    best_match = None
    best_score = 0

    for pokemon in pokemon_names:
        score = Levenshtein.distance(pokemon, target)

        if best_match is None or score< best_score:
            best_match = pokemon
            best_score = score

    return best_match


openai.api_key = "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"
added_term = "Give me the 6 pokemon one after the other with 1 whitespace in between and no other text"
poke_response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
data = poke_response.json()

pokemon_names = [pokemon["name"] for pokemon in data["results"]]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": "Build me a pokemon team with a core of Hydreigion"+added_term
    }]
)
pokemon = response['choices'][0]['message']['content'].strip('."').split('\n')
pokemons = []
for p in pokemon:
    pokemons.append(getExactMatch(p, pokemon_names))

print(pokemon)
print(pokemons)