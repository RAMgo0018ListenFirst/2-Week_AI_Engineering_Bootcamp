import Footer from "./components/Footer"
import Navbar from "./components/Navbar"
import Card from "./components/Card"
function App() {
  const cardsData = [
    {
      title: "card 1",
      description: "card 1 desc"
    },
    {
      title: "card 2",
      description: "card 2 desc"
    },
    {
      title: "card 3",
      description: "card 3 desc"
    },
    {
      title: "card 4",
      description: "card 4 desc"
    }
  ]
  return (
    <>
      <Navbar />

      <div className="cards">
        {cardsData.map((card, index) => {
          return (
            <Card
              key={index}
              title={card.title}
              description={card.description}
            />
          )
        })}
      </div>
      <Footer />
    </>
  )
}
export default App
