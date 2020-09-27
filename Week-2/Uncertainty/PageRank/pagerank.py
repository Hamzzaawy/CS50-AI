import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    
    
    # print(corpus)
    # for key, value in corpus.items():
    #     print(key, ' : ', value)
    # print(f"the length is {len(corpus['2.html'])} ")

    # transition_model(corpus,'1.html',DAMPING)

    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # raise NotImplementedError
    k = (1 - damping_factor) / (len(corpus))
    # print(k)
    linkedPages = len(corpus[page])
    # print(linkedPages)
    output = dict()
    # output[page] = round(k,4)
    # for n in corpus[page]:
    #     output[n] = ((1 / linkedPages) * damping_factor + k)
    # output = sorted(output.items(), key=lambda x: x[0])
    for n in corpus:
        if n in corpus[page]:
            output[n] = ((1 / linkedPages) * damping_factor + k)
        else:
            output[n] = round(k,4)
    # print(output)
    return output
    


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    nextPage =  random.choice(list(corpus.keys()))
    # print(nextPage)
    sum = {}
    for page in corpus:
        sum[page] = 0
    for i in range(n):
        temp = transition_model(corpus,nextPage,damping_factor)
        nextPage = random.choices(list(temp.keys()), list(temp.values()), k=1)[0]
        for j in sum:
            sum[j] += temp[j]
        # sum += temp
    for j in sum:
        sum[j] = round(sum[j] / n, 4)

    return sum
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # raise NotImplementedError
    out = {}
    flag = True

    for page in corpus:
        out[page] = 1 / (len(corpus))

    # old_out = copy.deepcopy(out)
    # print (out)

    while flag:
        flag = False
        # print(f"the old  is{old_out}")
        # print(f"the new  is{out}")
        old_out = copy.deepcopy(out)
        for page in corpus:
            # print (page)
            out[page] = (1 - damping_factor) / len(corpus) + damping_factor * Sum_Fn(corpus,out,page)
            if (out[page] - old_out[page]) > 0.001:
                flag = True
            else:
                flag = False

    
    return out



def Sum_Fn(corpus,out,p):
    Sum = 0
    for page, links in corpus.items():
        # print(f"the page  is{p}")
        # print(f"the links are is{links}")
        if p in links:
            # print(corpus[p])
            numLinks = len(corpus[page])
            # print(numLinks)
            Pr = out[p]
            Sum += (Pr / numLinks)
    # print(F"the sum is{Sum}")        
    return Sum


        


    


if __name__ == "__main__":
    main()
