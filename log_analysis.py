#!/usr/bin/env python3

import psycopg2

# A function to connect to the DB, it will be invoked on every other function


def db_connect():
    DBNAME = "news"
    try:
        db = psycopg2.connect(database=DBNAME)
        conn = db.cursor()

        # Return tuple, DB connection and cursor
        return db, conn
    except:
        # If not able to connect throws error
        print("Unable to connect to the database")


def popular_articles():
    """
     This method will return a formatted string listing the
     most porpular articles based on their view amount
    """

    # Create a connection with DB
    db, connect = db_connect()

    connect.execute("""
                    SELECT articles.title, COUNT(log.path) AS views FROM log
                    JOIN articles ON log.path like '%' || articles.slug || ''
                    GROUP BY articles.title ORDER BY views DESC limit 3;
                    """)

    # Convert fetched result into a list
    result = list(connect.fetchall())

    output = "\t         The most viewed articles are: \n"

    for i in result:
        output += "\n \"" + i[0] + "\" -- " + str(i[1]) + " views \n"

    # Close connection with DB
    db.close()
    return output

# Most popular article authors of all time;
# which authors get the most page views.


def popular_authors():
    """
    This method returns a formatted string listing the popularity
    of authors based on their article's views
    """
    # Create a connection with DB
    db, connect = db_connect()

    connect.execute("""
                    SELECT authors.name, COUNT(authors.name) AS author_count,
                    authors.id FROM authors JOIN articles ON authors.id =
                    articles.author JOIN log ON log.path = '/article/' ||
                    articles.slug || '' GROUP BY authors.name, authors.id
                    ORDER BY authors.id;
                    """)

    result = list(connect.fetchall())
    output = "\n \t       The most popular article authors: \n"
    for j in result:
        output += "\n " + j[0] + " -- " + str(j[1]) + " views \n"

    # Close connection with DB
    db.close()
    return output

# On which days did more than 1% of requests lead to errors?


def errors_count():
    """
    This method returns all possible dates where the margin or error requests
    are were more than 1%.
    """

    # Create a connection with DB
    db, connect = db_connect()

    # Execute query against the DATABASE
    connect.execute("""
                    SELECT TO_CHAR(time::DATE, 'Mon DD, YYYY'), to_char(ROUND
                    (COUNT(status) FILTER (WHERE status != '200 OK')/CAST
                    (COUNT(status) AS DECIMAL) * 100, 2), '9.9') AS PERCNT
                    FROM log GROUP BY time::DATE ORDER BY PERCNT DESC;
                    """)

    # Create output variable to be return with final output of the function
    output = "\n \t       Days with more than 1% of Error: \n"

    # Fetch the result from the query
    result = connect.fetchall()

    # Extract and format result into the output variable
    for x in result:
        if float(x[1]) > 1:
            output += "\n - " + x[0] + " -- " + x[1] + "%. \n"

    # Close connection with DB
    db.close
    return output


def main():

    # Create file
    out_file = open('art_report.txt', 'a')

    # Write the returned output from each function into the file
    out_file.write(popular_articles())
    out_file.write(popular_authors())
    out_file.write(errors_count())

    # Close file
    out_file.close()

# execute main function to start the report's creation
if __name__ == '__main__':
    main()
