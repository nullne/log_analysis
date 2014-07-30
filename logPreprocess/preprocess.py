#! /usr/bin/python
# author:    nullne
# email:     co.crary@gmail.com
# Do:  
# TODO:
# -*- coding: utf-8 -*-

import sys
import re
import optparse
import ConfigParser

import arg


def main():
    #res store the results
    res = []

    #get the arguments
    args = arg.main()

    #get the config
    if args.config:
        configFile = args.config
    else:
        configFile = "matchPatterns.cfg"
    cfile = open(configFile, 'r')
    config = ConfigParser.SafeConfigParser()
    config.readfp(cfile)
    cfile.close()
    if config.has_option('DEFAULT', 'PATTERN'):
        PATTERN = [x.strip() for x in config.get('DEFAULT', 'PATTERN').splitlines() if x]
        logLine = re.compile(PATTERN[0], re.I)
    else:
        print "error"
        sys.exit(0)
    if config.has_option('DEFAULT', 'URLPATTERN'):
        URLPATTERN = [x.strip() for x in config.get('DEFAULT', 'URLPATTERN').splitlines() if x]
        urlNums = len(URLPATTERN)
        urlPattern = {}
        for u in URLPATTERN:
            urlPattern[u.split(',')[1]] = re.compile(u.split(',')[0], re.I)
    else:
        print "error"
        sys.exit(0)
    if config.has_option('DEFAULT', 'QUERYPATTERN'):
        QUERYPATTERN = [x.strip() for x in config.get('DEFAULT', 'QUERYPATTERN').splitlines() if x]
        queryNums = len(QUERYPATTERN)
        queryPattern = []
        for q in QUERYPATTERN:
            queryPattern.append(re.compile(q, re.I))
    #filter Config
    if config.has_option("DEFAULT", "FILTERS"):
        filters = [x.strip() for x in config.get('DEFAULT', 'FILTERS').splitlines() if x]
    else:
        print "error"
        sys.exit(0)

    #read file
    # todo: error excep
    log = open(args.filename, 'r')
    cnt = 0
    errorCnt = 0
    keepCnt = 0
    postfixCnt = 0
    codeCnt = 0
    for l in log:
        original = l
        cnt += 1
        matches = logLine.match(l)
        if matches is None:
            errorCnt +=1
            print("Line %d doesn't match the required format\n%s" % (cnt, l))
            continue
        lineData = matches.groupdict()

        if lineData['code']:
            if lineData['code'] in ['401', '404']:
                codeCnt += 1
                continue
        #handle url
        if lineData['url']:
            url = lineData['url'].strip()
        else:
            continue
        #print "lines %d url:%s" % (cnt, url)
        #filter specific postfix
        stop = False
        for e in filters:
            if re.search(e, url, re.IGNORECASE) is not None:
                postfixCnt += 1
                stop = True
                break
        if stop:
            continue
        replacedUrl = url
        for up in urlPattern:
            replacedUrl,subNums = urlPattern[up].subn(up, replacedUrl)
        #handle querstring
        if lineData['querystring']:
            querystring = lineData['querystring'].strip()
            if querystring == '?':
                pass
            else:
                queryArray = querystring.split('&')
                queryArray[0] = queryArray[0][1:]
                replacedQuery = '?'
                for a in sorted(queryArray):
                    #if not matched,change to default
                    match = False
                    keyValue = a.split('=')
                    lenKeyValue = len(keyValue)
                    for p in queryPattern:
                        if p.search(a):
                            match = True
                            break
                    if not match:
                        match = False
                        if lenKeyValue == 2:
                            if re.match('^\d+$',keyValue[1],re.I):
                                continue
                            keyValue[1] = keyValue[0] + '_const'
                        elif lenKeyValue == 1:
                            #print '1'
                            keyValue.append( keyValue[0] + '_const' )
                        elif lenKeyValue == 0:
                            print '0'
                            pass
                        else:
                            print 'other'
                            pass
                    replacedQuery = replacedQuery + '='.join(keyValue) + '&'
                #replace the matched portion
                l = l.replace(querystring, replacedQuery[:-1])
        l = l.replace(url, replacedUrl)
        if l == original:
            keepCnt +=1
        res.append(l)
    log.close()
    #write the results to new file
    newFileName = args.filename.replace(args.filename.split('/')[-1], ("res_" + args.filename.split('/')[-1])) 
    newFile = open(newFileName, 'a')
    for r in res:
        newFile.write(r)
    newFile.close()

    print "All %d lines: \n   %d lines were processed \n   %d lines were filtered \n   %d lines came errors \n The results  are stored in %s" % (cnt, cnt-keepCnt-errorCnt-codeCnt, codeCnt, errorCnt, newFileName)



if __name__ == '__main__':
    main()
