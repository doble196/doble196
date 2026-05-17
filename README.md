<div align="center">

# Rensley R.

**Founder, builder, and platform engineer — New York, NY**

Building the [GitHat](https://www.githat.io) platform: a fleet of AWS-native apps sharing one identity provider, one payments rail, and one deploy pattern.

[![Website](https://img.shields.io/badge/githat.io-000?style=for-the-badge&logo=safari&logoColor=white)](https://www.githat.io)
[![X](https://img.shields.io/badge/@VyperPilledDev-000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/VyperPilledDev)
[![Location](https://img.shields.io/badge/New_York-000?style=for-the-badge&logo=googlemaps&logoColor=white)]()

</div>

---

## The fleet

```mermaid
flowchart LR
    GitHat["🎩 GitHat<br/>identity"] -->|auth| Sebastn["💳 Sebastn<br/>payments"]
    GitHat -->|auth| ClickReserv["📅 ClickReserv<br/>bookings"]
    GitHat -->|auth| Quantl["📊 Quantl<br/>analytics"]
    GitHat -->|auth| Colmado["🛒 Colmado<br/>commerce"]
    Sebastn -->|Stripe Connect| ClickReserv
    Sebastn -->|Stripe Connect| Quantl

    classDef root fill:#0a0a0a,stroke:#fff,color:#fff
    classDef app fill:#1a1a1a,stroke:#888,color:#fff
    class GitHat root
    class Sebastn,ClickReserv,Quantl,Colmado app
```

Every app: **Route 53 → CloudFront → EC2 (Caddy → Node)** with auto-rotating ACM certs and CAA lockdown. No third-party CAs, no third-party CDNs.

## What I'm building

| App | Domain | What it does |
|---|---|---|
| **GitHat** | [githat.io](https://githat.io) | RS256/KMS identity provider for the fleet |
| **Sebastn** | [sebastn.com](https://sebastn.com) | Stripe Connect payments-as-a-service |
| **ClickReserv** | [reserv.click](https://reserv.click) | Multi-tenant booking SaaS (26 templates) |
| **Quantl** | [quantl.click](https://quantl.click) | Quant signals + forecasting |
| **Colmado** | [colmado.click](https://colmado.click) | Commerce |

## Stack I ship with

[![Next.js](https://img.shields.io/badge/Next.js_16-000?logo=nextdotjs)](https://nextjs.org)
[![React](https://img.shields.io/badge/React_19-000?logo=react)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-000?logo=typescript)](https://www.typescriptlang.org)
[![Tailwind](https://img.shields.io/badge/Tailwind_4-000?logo=tailwindcss)](https://tailwindcss.com)
[![Node](https://img.shields.io/badge/Node_20-000?logo=nodedotjs)](https://nodejs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-000?logo=postgresql)](https://www.postgresql.org)
[![AWS](https://img.shields.io/badge/AWS-000?logo=amazonaws)](https://aws.amazon.com)
[![CloudFront](https://img.shields.io/badge/CloudFront-000?logo=amazonaws)](https://aws.amazon.com/cloudfront)
[![Lambda](https://img.shields.io/badge/Lambda-000?logo=awslambda)](https://aws.amazon.com/lambda)
[![SES](https://img.shields.io/badge/SES-000?logo=amazonaws)](https://aws.amazon.com/ses)
[![Stripe](https://img.shields.io/badge/Stripe_Connect-000?logo=stripe)](https://stripe.com/connect)
[![Solidity](https://img.shields.io/badge/Solidity-000?logo=solidity)](https://soliditylang.org)
[![Foundry](https://img.shields.io/badge/Foundry-000?logo=foundry)](https://getfoundry.sh)

## Approach

- **AWS-native edge** — Route 53 + CloudFront + ACM, no Cloudflare, no Let's Encrypt
- **One identity provider** — RS256/JWKS, KMS-backed, no shared secrets between apps
- **Stripe Connect** — businesses onboard as connected accounts under Sebastn's platform
- **AI-native developer experience** — every repo ships with `CLAUDE.md` and MCP server hooks where it matters
- **Standalone Next.js on t2.micro** — sized for unit economics, not vanity

## Stats

<div align="center">

![GitHub stats](https://github-readme-stats.vercel.app/api?username=doble196&show_icons=true&theme=tokyonight&hide_border=true&bg_color=00000000)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=doble196&layout=compact&theme=tokyonight&hide_border=true&bg_color=00000000)

</div>

---

<div align="center">
<sub>Currently shipping <a href="https://reserv.click">ClickReserv</a> · find me at <a href="https://www.githat.io">githat.io</a></sub>
</div>
