package database

import org.jetbrains.exposed.sql.Database

class PostgresHandler {

    /**
     * Connects to the specified database.
     */
    private fun connect() {
        Database.connect(
            "localhost", // TODO: Pass this in for testing
            driver = "org.postgresql.Driver"
        )
    }

    private fun createTables() {

    }
}