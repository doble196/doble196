<div align="center">

# Rensley R.

**Founder, builder, platform engineer — New York, NY**

Building [GitHat](https://www.githat.io): a fleet of apps sharing one identity layer, one payments rail, one deploy story.

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
    Sebastn -->|payments| ClickReserv
    Sebastn -->|payments| Quantl

    classDef root fill:#0a0a0a,stroke:#fff,color:#fff
    classDef app fill:#1a1a1a,stroke:#888,color:#fff
    class GitHat root
    class Sebastn,ClickReserv,Quantl,Colmado app
```

Single edge pattern across every app. Certs auto-rotate. No third-party CAs.

## What I'm building

| App | Domain | What it does |
|---|---|---|
| **GitHat** | [githat.io](https://githat.io) | Identity layer for the fleet |
| **Sebastn** | [sebastn.com](https://sebastn.com) | Payments rail |
| **ClickReserv** | [reserv.click](https://reserv.click) | Multi-tenant booking SaaS |
| **Quantl** | [quantl.click](https://quantl.click) | Quant signals + forecasting |
| **Colmado** | [colmado.click](https://colmado.click) | Commerce |

## How I ship

- **Cloud-native edge** — one pattern, every app, certs auto-rotate
- **One identity provider** — verified locally, no shared secrets between apps
- **One payments rail** — businesses onboard as connected accounts
- **AI-native dev loop** — every repo ships with agent metadata
- **Sized for unit economics** — not vanity

## Stats

<div align="center">

![Metrics](./metrics.svg)

</div>

---

<div align="center">
<sub>Currently shipping <a href="https://reserv.click">ClickReserv</a> · <a href="https://www.githat.io">githat.io</a></sub>
</div>
