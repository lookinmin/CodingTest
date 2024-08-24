/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function (secret, guess) {
  let bulls = 0;
  let cows = 0;

  const secretCount = new Array(10).fill(0);
  const guessCount = new Array(10).fill(0);

  // Step 1: Calculate bulls and prepare counts for cows
  for (let i = 0; i < secret.length; i++) {
    if (secret[i] === guess[i]) {
      bulls++;
    } else {
      secretCount[secret[i]]++;
      guessCount[guess[i]]++;
    }
  }

  // Step 2: Calculate cows based on counts
  for (let i = 0; i < 10; i++) {
    cows += Math.min(secretCount[i], guessCount[i]);
  }

  return `${bulls}A${cows}B`;
};
