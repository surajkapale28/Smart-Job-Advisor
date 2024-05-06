def accept_or_reject_resume(resume):
    keyword_list = ["python", "machine learning", "communication"]
    resume_keywords = set(resume.lower().split())
    job_keywords = set(keyword_list)

    common_keywords = resume_keywords.intersection(job_keywords)

    # Adjust the threshold based on the number of common keywords you desire
    threshold = 2  # Example threshold

    if len(common_keywords) >= threshold:
        return "Accept"
    else:
        return "Reject"
    

# Example usage:


