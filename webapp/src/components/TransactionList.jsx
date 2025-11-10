import { useEffect, useState } from "react"
import { queryGraphQL, createTransaction } from "../api"

export default function TransactionList({ accountNumber }) {
  const [txns, setTxns] = useState([])

  useEffect(() => {
    if (accountNumber) loadTxns()
  }, [accountNumber])

  const loadTxns = async () => {
    const data = await queryGraphQL(accountNumber)
    setTxns(data.data.transactions)
  }

  const handleNewTxn = async () => {
    await createTransaction({ account_number: accountNumber, amount_cents: 500, memo: "New deposit" })
    await loadTxns()
  }

  if (!accountNumber) return <p>Select an account above</p>

  return (
    <div>
      <h3>Transactions (from FastAPI GraphQL)</h3>
      <button onClick={handleNewTxn}>Create Test Transaction</button>
      <ul>
        {txns.map(t => (
          <li key={t.id}>
            {t.amount_cents > 0 ? "Deposit" : "Withdrawal"} — {t.amount_cents / 100} USD ({t.memo})
          </li>
        ))}
      </ul>
    </div>
  )
}
