const readline = require('readline');

// This function gets user input. Ignore the Promise details, it's unimportant
function getNum(questionText) {
  return new Promise((resolve, reject) => {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    rl.question(questionText, (answer) => {
      rl.close();
      if (answer === '' || isNaN(parseInt(answer))) {
        // keep asking the question until we get a valid answer
        console.log('That is not a number!');
        getNum(questionText).then(resolve);
      } else {
        resolve(parseInt(answer));
      }
    });
  });
}

async function main() {
  let acc = 0;
  let num = 0;
  let nums = [];

  num = await getNum('How many snakes are there? ');
  acc = acc | num & 0xff;
  nums.push(num);

  num = await getNum('How many ladders are there? ');
  acc = acc | (num & 0xff) << 8;
  nums.push(num);

  acc = acc | acc << 16;

  num = await getNum('How many chutes are there? ');
  acc = acc ^ (num & 0xff) << 13;
  nums.push(num);

  num = await getNum('How many escalators are there? ');
  acc = acc ^ (num & 0xff) << 49;
  nums.push(num);

  if (acc === 543056050) {
    console.log('You win!');

    let flagEncrypted = [208, 17, 54, 47, 225, 72, 81, 62, 134, 78, 83, 55, 211, 110, 87];
    let flag = '';
    for (let i = 0; i < flagEncrypted.length; i++) {
      flag += String.fromCharCode(flagEncrypted[i] ^ nums[i % nums.length]);
    }
    console.log(`The flag is: sigpwny{${flag}}`);
  } else {
    console.log('Nope');
  }
}

main().then();
