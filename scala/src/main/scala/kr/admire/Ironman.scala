package kr.admire

object MapReduce {
  def collect[T](mappedData: List[(Set[T], Long)]): Map[Set[T], List[Long]] = {
    return mappedData.groupBy(_._1).mapValues(_.map(_._2))
  }

  def apply[T](data: List[Set[T]], mapReducer: MapReducer): Map[Set[T], Long] = {
    return mapReducer.reducer(collect(mapReducer.mapper(data)))
  }
}

trait MapReducer {
  def mapper[T](data: List[Set[T]]): List[(Set[T], Long)]

  def reducer[T](mappedData: Map[Set[T], List[Long]]): Map[Set[T], Long] = mappedData.mapValues(_.reduce(_ + _))
}

class FrequencyItemMapReducer extends MapReducer {
  override def mapper[T](data: List[Set[T]]): List[(Set[T], Long)] = {
    val res: Iterable[(Set[T], Long)] = for {
      setData <- data
      item <- setData
    } yield (Set[T](item), 1: Long)

    return res.toList
  } 
}

class FrequencyItemForMapReducer[U](_for: List[Set[U]]) extends MapReducer {
  def mapper[T](data: List[Set[T]]): List[(Set[T], Long)] = {
    val _for = this._for.asInstanceOf[List[Set[T]]]
    val res = for {
      tSet <- data
      cSet <- _for.asInstanceOf[List[Set[T]]]
      if cSet.subsetOf(tSet)
    } yield (cSet, 1: Long)

    return res.toList
  }
}

object Ironman {
  def getFrequency[T](data: List[Set[T]]): Map[Set[T], Long] = {
    return MapReduce(data, new FrequencyItemMapReducer())
  }

  def getFrequencyFor[T](_for: List[Set[T]],
                         data: List[Set[T]]): Map[Set[T], Long] = {
    return MapReduce(data, new FrequencyItemForMapReducer(_for))
  }
}
