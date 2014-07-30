#! /usr/bin/python
# -*- coding: utf-8 -*-

# "172.16.245.69 - - [11/Apr/2011:16:06:10 +0200] GET /URL HTTP/1.1" 200 55 7/7124818
# "172.16.245.69 - - [11/Apr/2011:16:06:10 +0200] GET /URL HTTP/1.1" 304 - 0/15625

import sys
import re
import optparse
import logging
import operator
import os.path
import os
import psycopg2
import ConfigParser
from datetime import datetime, date, time, timedelta
import time

import pages



# greedy
#PATTERN = r"""[^[]*\[(?P<date>\d\d/\w*/\d{4})\:(?P<time>\d\d\:\d\d\:\d\d)[^[]*\] "(?:GET|POST) (?P<url>[^?]*)(?P<querystring>\?.*)? HTTP/.*" (?P<code>\d\d\d).*(?P<sec>\d+)/(?P<micros>\d+)"""
# non-greedy
PATTERN = r""".*?(?P<ip>\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}) .*?\[(?P<date>.*?)\:(?P<time>\d\d\:\d\d\:\d\d).*?\].*? "(?P<querytype>GET|POST) (?P<url>.*?)(?P<querystring>\?.*?)? HTTP\/.*?" (?P<code>\d\d\d).*" (?P<micros>\d+)"""
#PATTERN = r""".*?\[(?P<date>.*?)\:(?P<time>\d\d\:\d\d\:\d\d).*?\] "(?:GET|POST) (?P<url>.*?)(?P<querystring>\?.*?)? HTTP\/.*?" (?P<code>\d\d\d).*(?P<sec>\d+)\/(?P<micros>\d+)"""
logLine = re.compile(PATTERN, re.I)

#PLANNAMEPATTERN = r"""\/plan\/\d+\/.*\/?"""
#planNamePattern = re.compile(PLANNAMEPATTERN)
def getPattern(cfg):
    config = ConfigParser.SafeConfigParser()
    config.read(cfg)
    if config.has_option('URL', 'pattern'):
        returns = [x.strip() for x in config.get('URL', 'pattern').splitlines() if x]
        if returns is None:
            print "no pattern found!"
            sys.exit(1)
        else:
            return returns

def fine():
    """
    res[url]['n'] = [pagename]
    res[url]['j'] = [pagename] """

    p = pages.main()
    res = {}
    
    for pagename in p:
        for url in p[pagename]:
            if p[pagename][url]['url_pattern'] not in res.keys():
                res[p[pagename][url]['url_pattern']] = {'j':[],'n':[]}
            if 'main' in p[pagename][url].keys():
                res[p[pagename][url]['url_pattern']]['j'].append(pagename)
                #print pagename,url
            else:
                res[p[pagename][url]['url_pattern']]['n'].append(pagename)
    return res
QUERYPATTERN = getPattern('queryPattern.cfg')
URL_PATTERN = pages.main()
urlAll = fine()

#NUMPATTERN = r"""/\d+\/?"""
#numPattern = re.compile(NUMPATTERN)
#URLPATTERN = [
#        ['/plan/planid/cases/', r"""\/plan\/\d+\/cases\/?""",],
#        ['/plan/planID/planName/', r"""\/plan\/\d+\/{1}.*""",],
#        ['/accounts/username/recent/', r"""\/accounts\/.*?\/recent\/?""",],
#        ['/accounts/username/bookmarks/', r"""\/accounts\/.*?\/bookmarks\/?""",],
#        ['/accounts/username/profile/', r"""\/accounts\/.*?\/profile\/?""",],
#        #['/idnumber/', r"""/\d+\/?""",],
#        ]
#
#urlPattern = []
#for name,pattern in URLPATTERN:
#    #urlPattern[name] = re.compile(pattern)
#    urlPattern.append([name, re.compile(pattern)])


DAY_PATTERN = r"""^(?P<day>today|yesterday|tomorrow|week|month|year)(?:(?P<modifier>\+|\-)(?P<qty>\d+))?$"""
dateControl = re.compile(DAY_PATTERN, re.I)

version = "1.4.0"
description = "Simple bash utility for analyze HTTP access log with enabled response time"

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

logger = logging.getLogger('TinyLogAnalyzer')
logging.basicConfig(level=logging.INFO)

HOME = os.path.expanduser('~')


def matchQuery(str):
    """
    """
    res = []
    str = str+ ' '
    for pattern in QUERYPATTERN:
        tmpPattern = '[\?&]' + pattern + '[ &]'
        line = re.compile(tmpPattern, re.I)
        matches = line.search(str)
        if matches is None:
            pass
        else:
            res.append(pattern)
            #return pattern
    if res:
        rs = ''
        res = sorted(res)
        for r in res:
            r = r + '&'
            rs += r
        return rs[:-1]
    else:
        return None
def query2list(str):
    """
    return list query pramas
    """
    res = str[1:].split('&')
    if res == ['']:
        res = None
    return res
def numeric_compare_total(x, y):
    return x['micros'] - y['micros']


def numeric_compare_average(x, y):
    return x['average'] - y['average']


def str2date(st):
    dd, mmm, yyyy = st.split('/')
    return date(int(yyyy), MONTHS.index(mmm) + 1, int(dd))


def str2datetime(st):
    """string date in format dd/Mon/aaaa:hh:mm:ss
    11/Apr/2011:16:06:10
    """
    dd, mmm, yyyy, hh, mm, ss = st[:2], st[3:6], st[7:11], st[12:14], st[15:17], st[18:20]
    return datetime(int(yyyy), MONTHS.index(mmm) + 1, int(dd), int(hh), int(mm), int(ss))


def parseDate(st):
    m = dateControl.match(st)
    if m:
        base = m.groupdict()['day']
        modifier = m.groupdict()['modifier']
        qty = m.groupdict()['qty']
        if base == 'today':
            resDate = date.today()
        elif base == 'yesterday':
            resDate = date.today() - timedelta(days=1)
        elif base == 'tomorrow':
            resDate = date.today() + timedelta(days=1)
        elif base == 'week':
            resDate = date.today()
            resDate -= timedelta(resDate.weekday())
        elif base == 'month':
            resDate = date.today()
            resDate -= timedelta(resDate.day - 1)
        # now modifiers (optional)
        if modifier and qty:
            qty = int(qty)
            if modifier == '+':
                resDate += timedelta(qty)
            else:
                resDate -= timedelta(qty)
        return resDate
    # dd/Mmm/aaaa
    return str2date(st)


def parseTime(st):
    try:
        hh, mm, ss = st.split(':')
    except ValueError:
        hh, mm = st.split(':')
        ss = 0
    return time(int(hh), int(mm), int(ss))


def reduceTime(seconds, td_diff, skip_time_start, skip_time_end, days_skipped):
    if td_diff.days > 0:
        if skip_time_start:
            t1 = parseTime(skip_time_start)
            amount1 = t1.hour * 3600
            amount1 += t1.minute * 60
            amount1 += t1.second
            seconds -= amount1 * td_diff.days
        if skip_time_end:
            t2 = parseTime(skip_time_end)
            amount2 = (24 - t2.hour) * 3600
            # let's REMOVE minutes and seconds
            amount2 -= t2.minute * 60
            amount2 -= t2.second
            seconds -= amount2 * td_diff.days
        if days_skipped:
            seconds -= (24 * 3600) * days_skipped
            # I already reduced the total for filter like skip_time_start and
            # skip_time_end, so... now I need to re-add them
            if skip_time_start:
                seconds += amount1 * days_skipped
            if skip_time_end:
                seconds += amount2 * days_skipped
    return seconds


def analyze(options, logfile):
    log = open(logfile)

    if options.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.CRITICAL)

    page = {}
    registry = {}
    unknownQuery = {}

    pageTopTotal = []
    pageTopAverage = []
    pageTopTimes = []
    topTotal = []
    topAverage = []
    topTimes = []
    lastProcessedDate = None
    lastProcessedTime = None
    days_skipped = 0

    first = True
    parsingStart = datetime.now()
    cnt = 0
    try:
        for l in log:
            cnt += 1
            matches = logLine.match(l)
            if matches is None:
                logger.warn("Line %d doesn't match the required format\n%s" % (cnt, l))
                continue

            lineData = matches.groupdict()
            ref_date = str2date(lineData['date'])

            # {'url': '/URL', 'sec': '7', 'code': '200', 'micros': '7124818'}
            url = lineData['url']
            if url.endswith('/') and url != '/':
                url = url[:-1]
#            for name, p in urlPattern:
#                url = p.sub(name, url)
#            url = numPattern.sub('/idnumber/', url)
#            #url = planNamePattern.sub('/plan/planId/planName/', url)
#            if url.endswith('/') and url != '/':
#                url = url[:-1]

            #filter useless query status code
            code = int(lineData['code'])
            if code == 401 or code == 500:
                continue

            curMicros = int(lineData['micros'])
            # min time check
            if options.min_time and curMicros < options.min_time * 1000:
                continue
            # max time check
            if options.max_time and curMicros > options.max_time * 1000:
                continue

            # query type
            if True:
                query_type = lineData['querytype']
                url = query_type + url

            # choosed to keep querystrings
            params_list = None
            if options.keep_query:
                querystring = lineData['querystring']
                if querystring:
                    params_list = query2list(querystring)
                    querystring = matchQuery(querystring)
                    if querystring is not None:
                        querystring = '?' + querystring
                        url += querystring
                        #print url
                    else:
                        #url = url + lineData['querystring']
                        if lineData['querystring'] not in unknownQuery.keys():
                            unknownQuery[lineData['querystring']] = url
                        else: pass

            # start date filters
            if options.start_date:
                start_date = parseDate(options.start_date)
                if ref_date < start_date:
                    continue

            # end date filters
            if options.end_date:
                end_date = parseDate(options.end_date)
                if ref_date > end_date:
                    # for the log isn't exactly time-continued
                    continue

            # include only...
            stop = False
            if options.includes:
                stop = True
                for i in options.includes:
                    if re.search(i, url, re.IGNORECASE) is not None:
                        stop = False
                        break
            if stop:
                continue

            # exclude all
            stop = False
            for e in options.excludes:
                if re.search(e, url, re.IGNORECASE) is not None:
                    stop = True
                    break
            if stop:
                continue

            # day filter: other times in the same day
            stop = False
            for dreg in options.skip_days:
                if re.search(dreg, lineData.get('date')) is not None:
                    stop = True
                    if lastProcessedDate and lineData.get('date') != lastProcessedDate:
                        logger.debug("Skipping %s due to filters" % lineData.get('date'))
                        days_skipped += 1

            if lastProcessedDate and lineData.get('date') != lastProcessedDate and not stop:
                logger.debug("...now analyzing %s" % lineData.get('date'))

            lastProcessedDate = lineData.get('date')
            lastProcessedTime = lineData.get('time')

            if stop:
                continue

            # not before time
            if options.skip_time_start:
                refTime = parseTime(options.skip_time_start)
                lastTime = parseTime(lastProcessedTime)
                if lastTime < refTime:
                    continue

            # not after time
            if options.skip_time_end:
                refTime = parseTime(options.skip_time_end)
                lastTime = parseTime(lastProcessedTime)
                if lastTime > refTime:
                    continue

            if first:
                print "Starting from %s:%s" % (lastProcessedDate, lastProcessedTime)
                firstDateTime = str2datetime("%s:%s" % (lastProcessedDate, lastProcessedTime))
                first = False

            url = url.replace('.','@') 
            if not registry.get(url):
                registry[url] = {'micros': curMicros, 'times': 1, 'url': url}
            else:
                registry[url]['micros'] = registry[url]['micros'] + curMicros
                registry[url]['times'] += 1

            # keep the three decimal points

            # data for statistics
            registry[url]['average'] = registry[url]['micros'] / registry[url]['times']
        #page based output
        #print 'register url', registry

        #print 'registry.keys:', registry.keys()
        for pagename in URL_PATTERN:
            #print 'pagename:', pagename
            page_tmp = {
                    'micros':0,
                    'times':0,
                    'average':0,
                    }
            #print pagename
            for  urlname in URL_PATTERN[pagename]:
                #print 'urlname', urlname
                params_string = ''
                if URL_PATTERN[pagename][urlname]['get_params']:

                    params = sorted(URL_PATTERN[pagename][urlname]['get_params'])
                    for param in params:
                        param += '&'
                        params_string += param
                    params_string = '?' + params_string
                    params_string = params_string[:-1]

                key = '%s%s%s' % (URL_PATTERN[pagename][urlname]['type'], URL_PATTERN[pagename][urlname]['url_pattern'], params_string)
                #print 'key:', key
                if key in registry.keys():
                    #print key
                    #print "again"
                    page_tmp['average'] += registry[key]['average']
                    if 'main' in URL_PATTERN[pagename][urlname].keys():
                        page_tmp['times'] = registry[key]['times']
                    page_exist = True
                else:
                    page_exist = False
                    #print "not matched pagename:", pagename
                    #print "stop by here:", key
                    break
            #add new recored
            if page_exist:
                #print 'again', pagename
                page_tmp['micros'] = page_tmp['times'] * page_tmp['average']
                #print 'page_tmp', page_tmp
                page[pagename] = page_tmp
                page_tmp = None
                page_exist = False
        #ajdust page called times
        def adjustTimes(pagename, times, deadline):
            deadline -=1
            if deadline < 0:
                return times 
            mainUrl = None
            for urlname in URL_PATTERN[pagename]:
                if 'main' in URL_PATTERN[pagename][urlname].keys():
                    mainUrl = URL_PATTERN[pagename][urlname]['url_pattern']
            # need error handler
            if mainUrl is None:
                print URL_PATTERN[pagename]
                print pagename
                print "error: no Main Url"
            if not len(urlAll[mainUrl]['n']):
                #print "yes"
                pass 
            else:
                minorTimes = 0
                for p in urlAll[mainUrl]['n']:
                    if p not in page:
                        continue
                    minorTimes += adjustTimes(p, page[p]['times'], deadline)
                    #print 'minorTimes:', minorTimes
                #reduce the minor time
                times = times - minorTimes
            #major times
            numsMajor = len(urlAll[mainUrl]['j'])
            #decimal places 
            return (times / numsMajor)

        for pagename in page:
            page[pagename]['times'] = adjustTimes(pagename, page[pagename]['times'], 5)
            if page[pagename]['times'] < 0:
                page[pagename]['times'] = 0
       # print 'page:', page


        for u in unknownQuery:
            #print "unknow:", unknownQuery[u],u
            pass

    except KeyboardInterrupt:
        # first CTRL+C don't stop the program
        print "\nEnough... stopped by user action"
    except:
        logger.exception("Error parsing log at line %d\n%s" % (cnt, l))
        raise

    # ****** now collect page data ************
    for m, record in page.items():
            #Top total time
            record['pagename'] = m
            #print record
            try:
                pageTopTotal.index(record)
            except ValueError:
                pageTopTotal.append(record)
                pageTopTotal.sort(key=operator.itemgetter("micros"), reverse=True)
                #print 'sort key:', operator.itemgetter("micros")
                pageTopTotal = pageTopTotal[:options.size]

            #Top total average
            record['pagename'] = m
            try:
                pageTopAverage.index(record)
            except ValueError:
                pageTopAverage.append(record)
                pageTopAverage.sort(key=operator.itemgetter("average"), reverse=True)
                pageTopAverage = pageTopAverage[:options.size]

            #Top called  times
            record['pagename'] = m
            try:
                pageTopTimes.index(record)
            except ValueError:
                pageTopTimes.append(record)
                pageTopTimes.sort(key=operator.itemgetter("times"), reverse=True)
                pageTopTimes = pageTopTimes[:options.size]

    # ******* now collect statistical data *******
    for m, record in registry.items():
            # Top total time
            try:
                topTotal.index(record)
            except ValueError:
                topTotal.append(record)
                topTotal.sort(numeric_compare_total, reverse=True)
                topTotal = topTotal[:options.size]

            # Top call times
            try:
                topTimes.index(record)
            except ValueError:
                topTimes.append(record)
                topTimes.sort(key=operator.itemgetter("times"), reverse=True)
                topTimes = topTimes[:options.size]

            # top average time
            if not options.min_times or options.min_times <= record['times']:
                try:
                    topAverage.index(record)
                except ValueError:
                    topAverage.append(record)
                    topAverage.sort(numeric_compare_average, reverse=True)
                    topAverage = topAverage[:options.size]

    log.close()
    requiredTime = datetime.now() - parsingStart

    if first:
        # no row parsed at all
        print "No row parsed in the given range"
        sys.exit(0)

    lastDateTime = str2datetime("%s:%s" % (lastProcessedDate, lastProcessedTime))

    print "Ending at %s:%s" % (lastProcessedDate, lastProcessedTime)
    print "Elapsed time: %s" % requiredTime
    td_diff = lastDateTime - firstDateTime
    print 'lastDateTime', lastDateTime
    print 'firstDateTime', firstDateTime
    diff_seconds = (td_diff.microseconds + (td_diff.seconds + td_diff.days * 24 * 3600) * 10 ** 6) / 10 ** 6
    #diff_seconds = 100


    # if I use skip-timeperiod_start/end I need to remove values from this list
    if options.skip_time_start or options.skip_time_end or options.skip_days:
        diff_seconds = reduceTime(diff_seconds, td_diff, options.skip_time_start, options.skip_time_end, days_skipped)
        print "Timedelta is %s (but only %s are counted due to time bounds)" % (td_diff, timedelta(seconds=diff_seconds))
    else:
        print "Timedelta is %s (%s seconds)" % (td_diff, diff_seconds)
    print ""

    if options.text:

        #print the results
        f = open('/tmp/./res.txt', 'wb')

        tnow = datetime.now()
        f.write("Manipulating time %s\n" % tnow)
        f.write("Top page called times\n")
        #print "Top page called times"
        cnt = 0
        pageTopTotalTimes = 0
        pageTopTotalMicros = 0
        for x in pageTopTimes:
            pageTopTotalTimes += x['times']
            pageTopTotalMicros += x['micros']
        if pageTopTotalTimes == 0:
            pageTopTotalTimes = 1
        if pageTopTotalMicros == 0:
            pageTopTotalMicros = 1
            
        for x in pageTopTimes:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, average %0.3f, %0.2f%% of the total)\n" % (
                               cnt,
                               x['pagename'],
                               float(x['micros']) / (10 ** 6),
                               x['times'],
                               float(x['average']) / (10 ** 6),
                               float(x['times']) * 100 / pageTopTotalTimes
                               ))
        #print ""
        f.write('\n')
        f.write('Top page total time\n')
        #print "Top page total time"
        cnt = 0
        for x in pageTopTotal:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, average %0.3f, %0.2f%% of the total)\n" % (
                               cnt,
                               x['pagename'],
                               float(x['micros']) / (10 ** 6),
                               x['times'],
                               float(x['average']) / (10 ** 6),
                               float(x['micros']) *100 / pageTopTotalMicros,
                               ))
        #print ""
        #print "Top page average time"
        f.write('\n')
        f.write('Top page average time')
        cnt = 0
        for x in pageTopAverage:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, average %0.3f)\n" % (
                               cnt,
                               x['pagename'],
                               float(x['micros']) / (10 ** 6),
                               x['times'],
                               float(x['average']) / (10 ** 6),
                               ))
        #print ""
        #print "Top total time"
        f.write('\n')
        f.write('Top total time\n')
        cnt = 0
        for x in topTotal:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, average %0.3f, %0.2f%% of the total)\n" % (
                               cnt,
                               x['url'],
                               float(x['micros']) / (10 ** 6),
                               x['times'],
                               float(x['micros']) / x['times'] / (10 ** 6),
                               (float(x['micros']) / (10 ** 6)) * 100 / float(diff_seconds),
                               ))
        #print ""
        #print "Top call times"
        f.write('\nTop call times\n')
        cnt = 0
        for x in topTimes:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, %d total)\n" % (
                              cnt,
                              x['url'],
                              float(x['average']) / (10 ** 6),
                              x['times'],
                              float(x['average']) / (10 ** 6) * x['times'],
                              ))
        #print ""
        #print "Top average time"
        f.write('\n Top average time')
        cnt = 0
        for x in topAverage:
            cnt += 1
            f.write( "  %04d - %s %0.3f (%d times, %d total)\n" % (
                              cnt,
                              x['url'],
                              float(x['average']) / (10 ** 6),
                              x['times'],
                              float(x['average']) / (10 ** 6) * x['times'],
                              ))

        f.close()
        print "The results was stored in /tmp/res.text"
    #connect database
    if options.sql:
        con = None
        #startTimePostgre = time.mktime(firstDateTime.timetuple())
        #endTimePostgre = time.mktime(lastDateTime.timetuple())
        startTimePostgre = firstDateTime
        endTimePostgre = lastDateTime
        nowPostgre = datetime.now()
        #connect to db and select names
        try:
            con = psycopg2.connect(database="log", user="redhat", password="redhat")
            cur = con.cursor()

            query = 'SELECT name FROM view_loganalysis'
            cur.execute(query)
            existName = cur.fetchall()
            existName = [e[0] for e in existName]

        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' %e
            sys.exit(1)
        finally:
            if con:
                con.close()


        if options.auto:

            namePostgre = 'log_' + str(date.today())
        else:
            namePostgre = raw_input("Please name this log analysis uniquely:\n")
            while namePostgre in existName:
                namePostgre = raw_input("Name need to be unique, Type again:\n")
        #insert datas
        try:
            con = psycopg2.connect(database="log", user="redhat", password="redhat")
            cur = con.cursor()

            # need to do better
            if options.auto:
                projectPostgre = 'TCMS'
            else:
                query = 'SELECT distinct(project) FROM view_loganalysis'
                cur.execute(query)
                projects = cur.fetchall()
                projects = ','.join([e[0] for e in projects])
                print projects
                projectPostgre = raw_input("Please input the project name(choose above existed or new one):\n")

            query = "INSERT INTO view_loganalysis(name, project, manipulate_time, start_time, end_time, page_config, query_config) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % (namePostgre, projectPostgre, nowPostgre, startTimePostgre, endTimePostgre, 'tcms 1.0', 'tcms 1.0')
            cur.execute(query)

            query = "SELECT id FROM view_loganalysis WHERE name='%s'" % namePostgre
            cur.execute(query)
            logID = cur.fetchone()[0]
            con.commit()

        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            sys.exit(1)

        finally:
            if con:
                con.close()
        try:
            con = psycopg2.connect(database="log", user="redhat", password="redhat")
            cur = con.cursor()

            pagePostgres = []
            for p in page:
                tmp = (p, format(page[p]['average'] / 1000000.0, '.3f'), page[p]['times'], format(page[p]['micros'] / 1000000.0, '.3f'))
                pagePostgres.append(tmp)
            query = "INSERT INTO view_entry(\"logAnalysis_id\", entry_type, name, average, times, micros) VALUES (" + str(logID) + ", 'page', %s, %s, %s, %s)"
            cur.executemany(query, pagePostgres)

            urlPostgres = []
            for p in registry:
                tmp = (p, format(registry[p]['average'] / 1000000.0, '.3f'), registry[p]['times'], format(registry[p]['micros'] / 1000000.0, '.3f'))
                urlPostgres.append(tmp)
            query = "INSERT INTO view_entry(\"logAnalysis_id\", entry_type, name, average, times, micros) VALUES (" + str(logID) + ", 'url', %s, %s, %s, %s)"
            cur.executemany(query, urlPostgres)
            con.commit()

        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            sys.exit(1)

        finally:
            if con:
                con.close()

def main():
    args = sys.argv[1:]

    defaults = {'size': 50, 'keep-query': False, 'min-time': 0, 'max-time': 0, 'min-times': 0,
                'start-date': None, 'end-date': None, 'skip-time-start': None, 'skip-time-end': None,
                'skip-timeperiod-start': None, 'skip-timeperiod-end': None,
                'includes': [], 'excludes': [], 'skip-days': [],
                'text': True, 'sql': False,
                }

    # Load user default settings
    if '-U' not in args and os.path.exists('./tinylogan.cfg'):
        cfile = open('./tinylogan.cfg', 'r')
        config = ConfigParser.SafeConfigParser()
        config.readfp(cfile)
        cfile.close()

        # I need to fake-read the argument -c now
        if '-c' in args:
            config_profile = args[args.index('-c') + 1]
            if not config.has_section(config_profile):
                print 'Section "%s" not found in %s' % (config_profile, './tinylogan.cfg')
                sys.exit(1)
        else:
            config_profile = 'DEFAULT'

        # numerical
        for param in ('size', 'min-time', 'max-time', 'min-times', ):
            if config.has_option(config_profile, param):
                defaults[param] = config.getint(config_profile, param)
        # boolean
        for param in ('keep-query', ):
            if config.has_option(config_profile, param):
                defaults[param] = config.getboolean(config_profile, param)
        # strings
        for param in ('start-date', 'end-date', 'skip-timeperiod-start', 'skip-timeperiod-end', ):
            if config.has_option(config_profile, param):
                defaults[param] = config.get(config_profile, param)
        # multis
        for param in ('includes', 'excludes', 'skip-days'):
            if config.has_option(config_profile, param):
                defaults[param] = [x.strip() for x in config.get(config_profile, param).splitlines() if x]

    usage = "usage: %prog [options] logfile"
    p = optparse.OptionParser(usage=usage, version="%prog " + version, description=description,
                              prog="tinylogan")
    p.remove_option("--help")
    p.add_option('--help', '-h', action="store_true", default=False, help='show this help message and exit')
    p.add_option('--verbose', '-v', action="count", default=0, help='verbose output during log analysis')
    p.add_option('--size', '-s', type="int", dest="size", default=defaults['size'],
                 help="choose the number of record to store in every log")
    p.add_option('--auto', '-a', action="store_true", dest="auto", default=False,
                 help="Please do not add this arguments unless you run an automated script")
    p.add_option('--sql', '-S', action="store_true", dest="sql", default=defaults['sql'],
                 help="Store the results in database")
    p.add_option('--text', '-T', action="store_true", dest="text", default=defaults['text'],
                 help="Store the results in plain text, location is ./log/res.txt")
    p.add_option('--keep-query', '-q', dest="keep_query", default=defaults['keep-query'], action="store_true",
                 help="keep query strings in URLs instead of cutting them. "
                      "Using this an URL with different query string is treat like different URLs.")
    p.add_option('--include', '-i', dest="includes", default=defaults['includes'], action="append", metavar="INCLUDE_REGEX",
                 help="a regexp expression that an URLs must match of will be discarded. "
                      "Can be called multiple times, expanding the set")
    p.add_option('--exclude', '-e', dest="excludes", default=defaults['excludes'], action="append", metavar="EXCLUDE_REGEX",
                 help="a regexp expression that an URLs must not match of will be discarded. "
                      "Can be called multiple times, reducing the set")
    p.add_option('--skip-day', dest="skip_days", default=defaults['skip-days'], action="append", metavar="SKIP_DAY",
                 help="A regexp that repr specific whole day or a set of dates that must be ignored. Can be called multiple times")
    p.add_option('--min-time', type="int", dest="min_time", default=defaults['min-time'], metavar="MIN_TIME_MILLIS",
                 help="ignore all entries that require less than this amount of millisecs")
    p.add_option('--max-time', type="int", dest="max_time", default=defaults['max-time'], metavar="MAX_TIME_MILLIS",
                 help="ignore all entries that require more than this amount of millisecs")
    p.add_option('--min-times', type="int", dest="min_times", default=defaults['min-times'], metavar="MIN_TIMES",
                 help="set a minimum number of times that a entry must be found to be used in the \"Top average time\" statistic")

    group = optparse.OptionGroup(p, "Date filters",
                                    "For those kind of filters you need to specify a date.\n"
                                    "You are free to use a specific date in the format dd/mmm/aaaa, like "
                                    "\"24/May/2011\", but also some keywords for relative date like "
                                    "\"today\", \"yesterday\", \"tomorrow\", \"week\" and \"month\".\n"
                                    "Use of \"week\" and \"month\" mean referring to first day of the current "
                                    "week or month.\n"
                                    "You can also provide a numerical modifier using \"+\" or \"-\" followed by "
                                    "a day quantity\n"
                                    "(example: \"week-5\" for going back of 5 days from the start of the week)."
                                    )

    group.add_option('--start-date', dest="start_date", default=defaults['start-date'],
                 help="date where to start analyze and record")
    group.add_option('--end-date', dest="end_date", default=defaults['end-date'],
                 help="date where to end analyze and record")
    p.add_option_group(group)

    group = optparse.OptionGroup(p, "Time filters",
                                    "When a time is needed, you must enter it in the format hh:mm:ss or simply "
                                    "hh:mm, like \"09:21:30\" or \"09:21\".\n"
                                    "Those filter are used for skip record that are registered \"too late at night\" "
                                    "or \"too early in the morning\".")
    group.add_option('--skip-timeperiod-start', dest="skip_time_start", default=defaults['skip-timeperiod-start'],
                 help="do not analyse records before the given time")
    group.add_option('--skip-timeperiod-end', dest="skip_time_end", default=defaults['skip-timeperiod-end'],
                 help="do not analyse records later the given time")
    p.add_option_group(group)

    group = optparse.OptionGroup(p, "Default configuration profiles",
                                    "You can read a set of default configuration options from a \"tinylogan.cfg\" file "
                                    "placed in the user's home directory.\n"
                                    "If this file is found, parameters from the \"DEFAULT\" section are read, but you "
                                    "can also add other sections.\n"
                                    "You can always override those options from the command line."
                                    )
    # All foos below are ignored, we read them before the args parsing take place
    # We still need them for documentation and for evade argparse errors
    group.add_option('-c', dest="foo", default='default', metavar="PROFILE",
                 help="read a different profile section than DEFAULT")
    group.add_option('-U', dest="foo", default=False, action="store_true",
                 help="Ignore the user default profile file (if exists)")
    group.add_option('--example-profile', dest="example_profile", default=False, action="store_true",
                 help="Print out an example profile file, then exit. "
                      "You can put this output in a \".tinylogan\" file in the same directory, then customize it")

    p.add_option_group(group)

    options, arguments = p.parse_args(args)

    if options.example_profile:
        default_path = os.path.dirname(__file__)
        try:
            # distributed version
            f = open(os.path.join(default_path, 'profiles', 'example_profile.cfg'))
        except IOError:
            # will not fail only when calling the .py file directly
            f = open(os.path.join(default_path, 'example_profile.cfg'))
        print '\n'
        print f.read()
        f.close()
        sys.exit(0)

    if options.help or not arguments:
        p.print_help()
        sys.exit(0)

    try:
        analyze(options, arguments[0])
    except KeyboardInterrupt:
        print "Err, Your order.."
        sys.exit(1)

if __name__ == '__main__':
    main()
