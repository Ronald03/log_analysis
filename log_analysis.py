import psycopg2


result = ""
DBNAME = "news"

try:
    db = psycopg2.connect(database=DBNAME)
except:
    print("Unable to connect to the database")

# Create a connection to the data base
connect = db.cursor()

# Most popular three articles of all time;
# Which articles have been accessed the most?


def popular_authors(file):
    output = ""

# Use the global openned connection
    connect.execute("SELECT articles.title, COUNT(log.path) AS views FROM log "
                    "JOIN articles ON log.path like '%' || articles.slug || ''"
                    " GROUP BY articles.title ORDER BY views DESC limit 3;")

# This will hold the result from the query converted from tuple to array (this"
# will be a 2 dimensional array)
    result_arr = []

# This variable will hold the formatted data and ready to be added to the
# output file
    output = "\n         The most viewed articles are: \n"
    file.write("\t         The most viewed articles are: \n")

# save result from query by fetchinig it to the result variable
    result = list(connect.fetchall())

    for i in result:
        # Convert result of the query from tuple to list/array and add them to
        # result_arr; not really in use
        result_arr.append(list(i))

# Extract title and views and add them to a variable; it is already formatted
# with spaces and new lines:
        output += "\n " + i[0] + " -- " + str(i[1]) + " views \n \n"
        file.write("\n " + i[0] + " -- " + str(i[1]) + " views \n \n")

    popular_articles(file)

# Most popular article authors of all time;
# which authors get the most page views.


def popular_articles(file):
    output = ""
    connect.execute("SELECT authors.name, COUNT(authors.name) AS author_count,"
                    " authors.id FROM authors JOIN articles ON authors.id = "
                    "articles.author JOIN log ON log.path LIKE '%' ||"
                    " articles.slug || '' GROUP BY authors.name, authors.id "
                    "ORDER BY authors.id;")
    output += "\n       The most popular article authors: \n"
    file.write("\t       The most popular article authors: \n")
    result = list(connect.fetchall())
    for j in result:

        # print list(j)
        output += "\n " + j[0] + " -- " + str(j[1]) + " views \n \n"
        file.write("\n " + j[0] + " -- " + str(j[1]) + " views \n \n")

    errors_count(file)

# On which days did more than 1% of requests lead to errors?


def errors_count(file):
    output = ""
    connect.execute("SELECT TO_CHAR(time::DATE, 'Mon DD, YYYY'), to_char(ROUND"
                    "(COUNT(status) FILTER (WHERE status != '200 OK')/CAST"
                    "(COUNT(status) AS DECIMAL), 2) * 100, '9.9') AS PERCNT "
                    "FROM log GROUP BY time::DATE ORDER BY PERCNT DESC;")
    output += "\n       Days with more than 1% of Error: \n"
    file.write("\n       Days with more than 1% of Error: \n")
    result = connect.fetchall()
    for x in result:
        if float(x[1]) > 1:
            output += "\n - " + x[0] + " -- " + x[1] + "%. \n"
            file.write("\n - " + x[0] + " -- " + x[1] + "%. \n")
            file.write("\n")
    # return output


def main():

    # Hold string variable to hold returned result
    output_text = ""

    # Create file
    out_file = open('art_report.txt', 'a')

    popular_authors(out_file)

    out_file.close()

main()
