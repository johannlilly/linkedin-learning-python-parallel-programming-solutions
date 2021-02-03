import multiprocessing
import target_function
if __name__ == '__main__':
 Process_jobs = []
 for i in range(5):
     p = multiprocessing.Process \
     (target=target_function.function,args=(i,))
     Process_jobs.append(p)
     p.start()
     p.join()
