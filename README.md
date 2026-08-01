<div align="center">

# <!-- IDENTITY:name -->Rensley R.<!-- /IDENTITY:name -->

**Onchain builder — <!-- IDENTITY:location -->New York, NY<!-- /IDENTITY:location -->**

🛠️ <!-- IDENTITY:status -->building Access0x1 — open-source onchain payments<!-- /IDENTITY:status -->

[![X](https://img.shields.io/badge/@VyperPilledDev-000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/VyperPilledDev)
[![Access0x1](https://img.shields.io/badge/Access0x1-000?style=for-the-badge&logo=ethereum&logoColor=white)](https://github.com/Access0x1/Access0x1)
[![Location](https://img.shields.io/badge/New_York-000?style=for-the-badge&logo=googlemaps&logoColor=white)]()

</div>

---

> **Read this first.** I'm first a reasoning-and-logic developer — fullstack, leaning
> backend, which is where fintech lies. If the look isn't there, here are my words:
> **judge me on the logic and the complexity of the project before you judge the way
> my button looks.** Everything below is that argument, with receipts.

## 🏆 Verified ETHGlobal Hacker Pack holder

Not a claim — an on-chain credential. The `EG-HACKER` token, held on Optimism:

```js
// ETHGlobal Hacker Pack — onchain holder check (Optimism)
const { ethers } = require('ethers'); // npm install ethers
const provider = new ethers.JsonRpcProvider('https://mainnet.optimism.io');

const pack   = '0x32382a82d9faDc55f971f33DaEeE5841cfbADbE0'; // ETHGlobal Hacker Pack (EG-HACKER)
const wallet = '0x53c61cfb8128ad59244e8c1d26109252ace23d14';
const abi    = ['function balanceOf(address owner) view returns (uint256)'];

const held = await new ethers.Contract(pack, abi, provider).balanceOf(wallet);
console.log(`${wallet} ${held > 0n ? 'is' : 'is not'} a pack holder`); // → is  (balance: 1)
```

## What I'm building

**Access0x1** — an open-source onchain payments + identity rail. USD-priced crypto checkout from a single link: no code, no contract, no gas to manage. One shared, non-custodial router; exact fee-split; prices read from Chainlink feeds in-transaction.

<!-- IDENTITY:fleet_table -->
| App | Domain | Role |
|---|---|---|
| **Access0x1** | [github.com/Access0x1/Access0x1](https://github.com/Access0x1/Access0x1) | Open-source onchain payments + identity rail |
| **NFTeria** | [nfteria.click](https://nfteria.click) | Onchain commerce built on Access0x1 |
<!-- /IDENTITY:fleet_table -->

Most recently at **ETHGlobal** — shipped Access0x1 and won a prize from **ENS**.

## Stats

<div align="center">

![Metrics](./metrics.svg)

</div>

<!-- DYNAMIC:START -->
> ☀️ Summer ops — shipping under the sun.
>
> 📅 **1,850 days on GitHub** · 5 years, 25 days · 264 weeks
> _Last updated: 2026-08-01 (America/New_York)_
<!-- DYNAMIC:END -->

---

<div align="center">
<sub>Building in the open · <a href="https://github.com/Access0x1/Access0x1">Access0x1</a></sub>
</div>
