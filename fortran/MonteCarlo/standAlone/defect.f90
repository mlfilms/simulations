program defect
implicit none

character(100) :: buffer
integer :: N = 200, endT=1001
real(8) :: beta=.4
real(8), allocatable, dimension(:,:) :: grid
real(8) :: x,g
real(8),parameter :: PI = 4*atan(1.0_8)
character(12) :: fileNames

integer :: i,j,t

!read in arguments (g,beta,N,endT)
call getarg(1,buffer)
read(buffer,*), g

call getarg(2,buffer)
read(buffer,*),beta

call getarg(3,buffer)
read(buffer,*),N

call getarg(4,buffer)
read(buffer,*),endT



!Initial Random Grid
write(*,*) 'initialize grid'
allocate(grid(N,N))
!write(*,*) grid(N,N)
call random_seed()
do i=1,N
    do j=1,N
!        write(*,*) i,j
        call random_number(x)
        grid(i,j) = x*2*PI
    end do
enddo
write(*,*) 'metropolis algo. commence'
!Preform the metropolis algorithm with XY hamiltonian
do t=1,endT
    call metro(grid,beta,N)
    write(fileNames,'(A3,I0.3,A4)') 'out', t,'.dat'
    if (modulo(t,10) .eq. 0) then
        print *, trim(fileNames)
    endif
    open(1,file=fileNames)
    do i=1,N
        write(1,*) (grid(i,j), j=1,N)
    enddo
    close(1)
end do
!Write to File

deallocate(grid)
contains
    function hamXY(i,j,theta,g)
        integer :: i,j
        real(8):: theta
        real(8) :: g,hamXY
        real(8), dimension(3) :: x,y
        !write(*,*) 'hamxy', i,j
        x =(/ grid(modulo(i-2,N)+1,j),theta,grid(modulo(i,N)+1,j)/)
        y =(/ grid(i,modulo(j-2,N)+1),theta,grid(i,modulo(j,N)+1)/)
        hamXY = -g*(cos(x(2)-x(1))+cos(x(3)-x(2))+cos(y(2)-y(1))+cos(y(3)-y(2)))
        end function hamXY
    subroutine metro(state,beta,N)
        real(8) :: theta, thetaP,x,delE,E1,E2,beta
        integer :: N
        real(8), dimension(N,N) :: state
        do i=1,N
            do j=1,N
                call random_number(x)
                theta = state(i,j)
                thetaP = theta+(x*4-2)
               ! write(*,*) 'metro',i,j
                E1 = hamXY(i,j,theta,g)
                E2 = hamXY(i,j,thetaP,g)
                delE = E1-E2

                if (delE < 0) then
                    state(i,j) = thetaP
                else if (delE < exp(-delE*beta)) then
                    state(i,j) = thetaP
                end if
            end do
        end do
    end subroutine metro
            


end program defect
