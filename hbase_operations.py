import happybase

def hbase_example():
    # Connect to HBase
    connection = happybase.Connection('localhost')
    connection.open()

    # Create table
    if b'my_table' not in connection.tables():
        connection.create_table(
            'my_table',
            {'cf': dict()}
        )

    # Insert data
    table = connection.table('my_table')
    table.put(b'row1', {b'cf:col1': b'value1'})

    # Fetch data
    row = table.row(b'row1')
    print(row)

    connection.close()

if __name__ == "__main__":
    hbase_example()

