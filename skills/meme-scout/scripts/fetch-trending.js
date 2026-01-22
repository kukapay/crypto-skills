const https = require('https');
const vm = require('vm');

const timeframe = process.argv[2] || 'h24';
const urlMap = {
  m5: 'https://dexscreener.com/?rankBy=trendingScoreM5&order=desc',
  h1: 'https://dexscreener.com/?rankBy=trendingScoreH1&order=desc',
  h6: 'https://dexscreener.com/',
  h24: 'https://dexscreener.com/?rankBy=trendingScoreH24&order=desc'
};

const changeKey = timeframe;

const url = urlMap[timeframe];

https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const match = data.match(/window\.__SERVER_DATA\s*=\s*(\{.*?\});/s);
    if (match) {
      const code = 'data = ' + match[1];
      const sandbox = {data: null, URL: URL, Date: Date, undefined: undefined};
      vm.runInNewContext(code, sandbox);
      const pairs = sandbox.data.route.data.dexScreenerData.pairs.slice(0,10);
      pairs.forEach(p => {
        const change = p.priceChange[changeKey] || 0;
        console.log(`${p.baseToken.name} | ${p.chainId} | $${p.priceUsd} | ${change}% | ${p.baseToken.address}`);
      });
    } else {
      console.error('No __SERVER_DATA found');
    }
  });
}).on('error', err => console.error(err));</content>
<parameter name="filePath">./skills/meme-scout/scripts/fetch-trending.js