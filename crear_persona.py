from persona import persona

juan == persona("juan", "castellano", 15)
juan.mostrarpersona()

leidy = persona("leidy", "alvarez", 18)
leidy.mostarpersonas()

leidy.apellidos = "perez"
leidy.mostarpersonas()

juan = leidy

juan.mostarpersonas()