def get_input(word_type:str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun=get_input("noun")
game=get_input('game')


story = f"""
{noun}, is playing {game}.

"""

print(story)