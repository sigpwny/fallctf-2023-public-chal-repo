import sqlite3 from 'sqlite3';
import fs from 'fs';

export default function initDatabase() {
  const dbFilePath: string = 'database/pwnymon.db';

  // Read the JSON data from your file
  const jsonData: any[] = require('database/gen1.json');

  // Open a connection to the SQLite database or create a new one if it doesn't exist
  const db: sqlite3.Database = new sqlite3.Database(dbFilePath, (err: Error | null) => {
    if (err) {
      console.error('Error opening database:', err.message);
      return;
    }
    console.log('Connected to the database.');

    // Create the "pwnymon" table if it doesn't exist
    db.run(`
      CREATE TABLE IF NOT EXISTS pwnymon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        image TEXT,
      )
    `, (err: Error | null) => {
      if (err) {
        console.error('Error creating table:', err.message);
        return;
      }
      // console.log('Table "pwnymon" created.');

      // Insert data from the JSON file if the ID doesn't exist
      jsonData.forEach((pwnymon) => {
        db.get('SELECT id FROM pwnymon WHERE id = ?', [pwnymon.id], (err: Error | null, row: any) => {
          if (err) {
            console.error('Error checking for existing ID:', err.message);
            return;
          }

          if (!row) {
            // ID doesn't exist, insert the row
            db.run('INSERT INTO pwnymon (id, name, description, image) VALUES (?, ?, ?, ?)', [pwnymon.id, pwnymon.name, pwnymon.description, pwnymon.image], (err: Error | null) => {
              if (err) {
                console.error('Error inserting row:', err.message);
              } else {
                // console.log(`Inserted pwnymon with ID ${pwnymon.id}`);
              }
            });
          } else {
            // console.log(`pwnymon with ID ${pwnymon.id} already exists.`);
          }
        });
      });
    });
  });

  // Close the database connection when done
  // db.close((err: Error | null) => {
  //   if (err) {
  //     console.error('Error closing database:', err.message);
  //   } else {
  //     console.log('Database connection closed.');
  //   }
  // });
  return db;
}

export async function queryPwnymon(search: string) {
  const db = new sqlite3.Database('database/pwnymon.db');
  const pwnymons: Pwnymon[] = await new Promise((resolve, reject) => {
    db.all(`SELECT * FROM pwnymon WHERE name LIKE '%${search}%'`, (err: Error | null, rows: any[]) => {
      if (err) {
        console.error('Error querying database:', err.message);
        return reject(err);
      }
      const pwnymons: Pwnymon[] = rows.map(row => ({
        id: row.id,
        name: row.name,
        description: row.description,
        image: row.image,
      }));
      resolve(pwnymons);
    });
  });
  return pwnymons;
}