program tsunami

  implicit none
  
  ! declare variables -------------------
  integer :: i, n

  ! declare constants -------------------
  integer, parameter :: grid_size = 100
  integer, parameter :: num_time_steps = 100

  real, parameter :: dt = 1 ! time step [sec]
  real, parameter :: dx = 1 ! grid spacing [meters]
  real, parameter :: c = 1 ! phase speed [meters/sec]

  ! create height array
  real :: h(grid_size), dh(grid_size)

  ! set initial height distribution parameters
  integer, parameter :: icenter = 25
  real, parameter :: decay = 0.02

  ! set output format
  character(*), parameter :: fmt = '(i0,*(1x,es15.8e2))'

  ! initialize hinitial height array
  do concurrent (i=1:grid_size)
    h(i) = exp(-decay * (i - icenter)**2)
  end do



  print fmt, 0, h

  ! set the time loop that models wave motion
  time_loop: do n = 1, num_time_steps

    dh(1) = h(1) - h(grid_size)

    do concurrent (i = 2:grid_size)
      dh(i) = h(i) - h(i-1)
    end do

    do concurrent (i = 1:grid_size)
      h(i) = h(i) - c * dh(i) / dx * dt
    end do

    print fmt, n, h

  end do time_loop
end program tsunami
