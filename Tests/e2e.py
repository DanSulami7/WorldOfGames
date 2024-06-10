from selenium import webdriver
driver = webdriver.Chrome()
import re
import sys

def main_function():
    # url = "http://127.0.0.1:5001/Game"
    url = "http://localhost:8777/Game"
    test_result = test_scores_service(url)
    driver.quit()

    if test_result:
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)

def test_scores_service(url):
    try:
        driver.get(url)
        score_element = driver.find_element(
            by="xpath", value="/html/body/h1").text
        print(score_element)
        score_number = extract_number(score_element)
        print(score_number)

        score_value = int(score_number)

        # Check if the score is between 1 and 1000
        if 1 <= score_value <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        print("The Score Was Found")

def extract_number(text):
    # Define a regular expression pattern to match numbers
    pattern = r'\d+'
    # Search for the pattern in the text
    match = re.search(pattern, text)
    # If a match is found, return the matched text as an integer
    if match:
        return int(match.group())
    else:
        return None

main_function()

