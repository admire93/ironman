import org.specs2.mutable._

import kr.admire.Ironman

class IronmanSpec extends Specification {
  val transaction: List[Set[String]] = List[Set[String]](
    Set("a", "b", "c", "d"),
    Set("a", "b"),
    Set("b", "c", "d"),
    Set("b", "c"),
    Set("a", "b", "d"),
    Set("c", "d"),
    Set("b", "d")
  )

  "Ironman " should {
    
    "get frequency table " in {
      Ironman.getFrequency[String](transaction) === Map[Set[String], Long](
                                                      Set("a") -> 3,
                                                      Set("b") -> 6,
                                                      Set("c") -> 4,
                                                      Set("d") -> 5
                                                    ) 
    }
  }
}
