import logging
import requests
import threading

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(name)s] [%(threadName)s] [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

urls = [
    "https://www.notawebsite",
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
]
RESULTS = {}
results_lock = threading.Lock()

def check_url(url: str) -> None:
    logger.info(f"Checking if {url} is reachable")
    is_reachable = False
    try:
        response = requests.get(url)
        is_reachable = response.ok
    except requests.exceptions.RequestException as e:
        logger.error(f"Error while checking {url}: {e}")
    finally:
        with results_lock:
            RESULTS[url] = is_reachable

def main():
    threads = []
    logger.info("Checking if the following urls are reachable:")
    thread_cout = 0
    for url in urls:
        logger.info(url)
        thread_cout += 1
        thread = threading.Thread(target=check_url, args=(url,), name=f"Thread-{thread_cout}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    logger.info("Results:")
    for url, is_reachable in RESULTS.items():
        logger.info(f"{url} is {'' if is_reachable else 'not '}reachable")


if __name__ == "__main__":
    main()
