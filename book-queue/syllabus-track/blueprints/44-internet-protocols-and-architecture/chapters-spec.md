# Chapter specifications

**Private Blueprint only. Draft route: `hold-source`. Evidence: `tentative-source`. No sign-off.**

Each entry is a proposed chapter, not drafted prose.

## 1. One message across two networks

- **Observable capability:** Annotate what the sender, two routers, and receiver each know
- **Teaching blocks:** encapsulation; frames vs packets; endpoints vs next hops; header visibility
- **Original worked example to write:** A museum kiosk sends a status message to a remote exhibit desk through two fictional routers.
- **Assessable practice:** Fill a four-column hop ledger and circle which identifiers should remain constant.

## 2. Who is local, and what path wins?

- **Observable capability:** Select the next hop from a small address and route table
- **Teaching blocks:** prefix membership; default route; longest match; overlapping routes
- **Original worked example to write:** Two forwarding entries overlap for exhibit kiosks, and the database address falls in both.
- **Assessable practice:** Compute the selected entries for four addresses and explain one changed result after removing a route.

## 3. When a name resolves but delivery fails

- **Observable capability:** Locate an observed failure in the right layer
- **Teaching blocks:** name lookup; connections and datagrams; observations vs inference; control vs data evidence
- **Original worked example to write:** A supplied diagram shows a resolved name and no application acknowledgment.
- **Assessable practice:** Rank three causes and give one already-supplied datum that rules out the wrong layer.

## 4. Carry a real service requirement across domains

- **Observable capability:** Compare forwarding and service-quality choices with end-to-end assumptions
- **Teaching blocks:** interdomain routing policy; IPv6 coexistence; traffic classes; scaling
- **Original worked example to write:** A city museum's live and archived media streams share two service networks with different handling priorities.
- **Assessable practice:** Evaluate two hypothetical route and service-class proposals using supplied policy and latency tables; show what remains unmeasured.

## 5. Make the network argument

- **Observable capability:** Explain a packet path and competing diagnosis from synthetic evidence
- **Teaching blocks:** hop tables; failure timelines; alternate paths; residual uncertainty
- **Original worked example to write:** A temporary link loss and a stale note lead to two inconsistent accounts of a campus display outage.
- **Assessable practice:** Submit an annotated diagram, one counterexample, and a concise case for the best-supported account.
