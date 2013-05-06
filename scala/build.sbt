name := "Ironman"


description :=  "Apriori Algorithm"

version := "0.1"

scalaVersion := "2.10.0"

publishTo := Some(Resolver.file("file",  new File(Path.userHome.absolutePath+"/.m2/repository")))

libraryDependencies ++= Seq(
  "org.specs2" % "specs2_2.10" % "1.14"
)
