def authorize(auth,user_role,role):
    try:
        if auth ==True:
            if user_role==role:
                return True
            else:
                return False,'Wrong User'
        else:
            return False,'Not Login'
    except:
        return False,'Not Login'
