import wikipedia


def main():
    """Get user input for a page title and display the title, summary, and URL of the page."""
    print("Welcome to Wikipedia Search! Type 'exit' to quit.")
    page_title = input("Input the page title: ").strip()

    while page_title.lower() != "exit":
        if not page_title:
            print("Please enter a valid page title.")
        else:
            try:
                searched_page = wikipedia.page(page_title)
                print(f"\nTitle: {searched_page.title}")
                print(f"Summary: {searched_page.summary.split('.')[0]}.\n")  # Display only the first sentence
                print(f"URL: {searched_page.url}\n")
            except wikipedia.exceptions.DisambiguationError as e:
                print("\nThe query is ambiguous. Here are some suggestions:")
                for i, option in enumerate(e.options[:10], 1):  # Limit to 10 options for readability
                    print(f"{i}. {option}")
                print("Please refine your query.\n")
            except wikipedia.exceptions.PageError:
                print(f"\n'{page_title}' does not match any pages. Try another query!\n")
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}\n")

        page_title = input("Input the page title: ").strip()

    print("Goodbye! Thanks for using Wikipedia Search.")


if __name__ == "__main__":
    main()
