from serpapi import GoogleSearch

def get_similar_jobs(job_title):
    params = {
        'q': f'similar jobs to {job_title}',
        'api_key': '95e7773188487ac6b07561499a816e7713813d70b8578f79556bfa3b67d3b358',
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract and print relevant information from the search results
    for result in results['organic_results']:
        title = result.get('title', '')
        link = result.get('link', '')
        snippet = result.get('snippet', '')
        return(f'Title: {title}\nLink: {link}\nSnippet: {snippet}\n---\n')

