import json
import csv
import time

headings =['Post','Caption','Date','likesComment','IdFatherComment','IdChildComment','Username']
post = "B166OkVBPJR"
caption = " "
date = ''
likesComment = 0
idFatherComment = " "
idChildComment = " "
username = " "
with open('dataframe.csv', 'w', encoding='utf-8', newline='') as f:
    mywriter = csv.writer(f)
    mywriter.writerow(headings)
    row = []
    with open('comments.json') as json_file_comments, open('childComments.json') as json_file_child:
        pages = json.load(json_file_comments)
        children = json.load(json_file_child)
        for page in pages:
            commentSet = page['comments']
            for comment in commentSet:
                row = []
                caption = repr(comment['text'])
                date = time.ctime(comment['created_at'])
                likesComment = comment['comment_like_count']
                idFatherComment = comment['pk']
                idChildComment = "NONE"
                username = comment['user']['username']
                row = [post,caption,date,likesComment,idFatherComment,idChildComment,username]
                print(row)
                mywriter.writerow(row)
                if(comment['child_comment_count']!=0):
                    nestedcomments = []
                    for child in children:
                        if(child['parent_comment']['pk']==idFatherComment):
                            nestedcomments = child['child_comments']
                            for nested in nestedcomments:
                                nestedRow = []
                                captionNested = nested['text']
                                dateNested = time.ctime(nested['created_at'])
                                likesCommentNested = nested['comment_like_count']
                                idChildComment = nested['pk']
                                usernameNested = nested['user']['username']
                                nestedRow = [post,captionNested,dateNested,likesCommentNested,idFatherComment,idChildComment,usernameNested]
                                print(nestedRow)
                                mywriter.writerow(nestedRow)
