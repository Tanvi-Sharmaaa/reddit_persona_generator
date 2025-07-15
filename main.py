from reddit_scrapper import get_user_data
from persona_generator import generate_persona

def main():
    profile_url = input("Enter Reddit profile url: ").strip()
    user_data = get_user_data(profile_url)

    print(f"\nGenerating persona for: {user_data['username']}\n")

    persona = generate_persona(user_data['posts'],user_data['comments'])
    filename = f"{user_data['username']}_persona.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(str(persona.content))

    print(f"Persona saved to {filename}")

if __name__ == "__main__":
    main()