import sqlite3 from 'sqlite3';

export async function GET(request: Request) {
  // Get the search parameter "q" from the URL (or default to empty string)
  const searchParam = new URL(request.url).searchParams;
  const search = searchParam.get('q') ?? '';
  const pwnymons = await queryPwnymon(search);
  const body = JSON.stringify(pwnymons);
  return new Response(body, {
    headers: {
      'content-type': 'application/json',
    },
  });
}

async function queryPwnymon(search: string) {
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
        description: row.description.replace(/(\n|\f)/gm," "),
        image: row.image,
      }));
      resolve(pwnymons);
    });
  });
  return pwnymons;
}
