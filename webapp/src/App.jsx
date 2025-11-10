import { useState } from "react"
import AccountList from "./components/AccountList"
import TransactionList from "./components/TransactionList"

export default function App() {
  const [selectedAccount, setSelectedAccount] = useState(null)

  return (
    <div style={{ padding: 24, fontFamily: "sans-serif" }}>
      <h1>🏦 Bank Dashboard</h1>
      <AccountList onSelect={setSelectedAccount} />
      <TransactionList accountNumber={selectedAccount} />
    </div>
  )
}
